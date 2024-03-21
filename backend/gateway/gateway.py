"""
This module implements the MQTT IoT Gateway.
"""

import asyncio
import json
import ssl
from typing import List, Tuple

import aiohttp
import async_timeout
import asyncpg
from aiologger import Logger
from aiologger.handlers.files import AsyncFileHandler
from asyncio_mqtt import Client, MqttError
from jsonpath_ng import parse
from redis import asyncio as aioredis
from uuid import uuid4
from settings import settings
import logging

# Load configuration from JSON file
MQTT_HOST = settings.MQTT_HOST
MQTT_PORT = settings.MQTT_PORT
MQTT_USER = settings.MQTT_USER
MQTT_PASSWORD = settings.MQTT_PASSWORD
MQTT_TLS = settings.MQTT_TLS
if MQTT_TLS:
    tls_context = ssl.create_default_context()
else:
    tls_context = None
REDIS_URL = settings.REDIS_URL
orion_url = settings.ORION_URL
service = settings.FIWARE_SERVICE
service_path = settings.FIWARE_SERVICEPATH

host = settings.POSTGRES_HOST
user = settings.POSTGRES_USER
password = settings.POSTGRES_PASSWORD
database = settings.POSTGRES_DB
DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

# Configure logging
logging.basicConfig(level=settings.LOG_LEVEL.upper(),
                    format='%(asctime)s %(name)s %(levelname)s: %(message)s')


class MqttGateway(Client):
    """
    This class implements the MQTT IoT Gateway.
    This implementation is asynchronous and uses the MQTTv5 protocol.
    The advantage of asynchronous programming is that it allows for multiple tasks to be executed concurrently.
    In comparison to multithreading or multiprocessing, asynchronous programming is more lightweight and thus
    more efficient. This is especially important for IoT applications, where the gateway is often a small device
    with limited resources. While asynchronous programming is more difficult to implement, I believe that it is worth the effort.
    The disadvantage of asynchronous programming is that it is more difficult to debug and it is not as efficient for CPU-bound tasks (which is not the case here).
    """

    def __init__(self):
        super().__init__(hostname=MQTT_HOST)
        # Create gateway device
        self.mqtt_queue = asyncio.Queue()
        self.redis_queue = asyncio.Queue()
        self.workers = []  # List of worker tasks
        self.cache = aioredis.from_url(
            url=f"{REDIS_URL}/0"
        )  # Cache for storing datapoints with an LRU eviction policy (least recently used)
        self.notifier = aioredis.from_url(
            url=f"{REDIS_URL}/1"
        )  # Redis Stream for notifying the API about new datapoints
        self.conn = None  # Initialized in run()

    async def mqtt_worker(self) -> None:
        async with aiohttp.ClientSession() as worker_session:
            while True:
                try:
                    topic, payload = await self.mqtt_queue.get()
                    await self.process_mqtt_message(topic, payload, worker_session)
                    self.mqtt_queue.task_done()
                except Exception as e:
                    logging.error(e)
                    continue

    async def redis_worker(self, client: Client) -> None:
        while True:
            try:
                data = await self.redis_queue.get()
                await self.process_redis_message(data, client=client)
                self.redis_queue.task_done()
            except Exception as e:
                logging.error(e)
                continue

    async def start_workers(self, client: Client) -> None:
        mqtt_workers = [asyncio.create_task(self.mqtt_worker()) for _ in range(12)]
        redis_workers = [asyncio.create_task(self.redis_worker(client)) for _ in range(4)]
        await asyncio.gather(*(mqtt_workers + redis_workers))

    async def process_redis_message(
        self, message: bytes, client: Client
    ) -> None:
        """
        Processes a single Redis message.

        Args:
            message (Tuple[str, str, Client]): A tuple containing the command, the topic,
            and the MQTT client used by the gateway.
        """
        decoded_data = {k.decode(): v.decode() for k, v in message.items()}

        command = list(decoded_data.keys())[0]
        topic = list(decoded_data.values())[0]

        try:
            logging.info(f"Processing command: {command} {topic}")
            if command == "subscribe":
                await client.subscribe(topic)
                logging.info(f"Subscribed to {topic}")
            elif command == "unsubscribe":
                await client.unsubscribe(topic)
                logging.info(f"Unsubscribed from {topic}")
            elif command == "unsubscribe_all":
                datapoints = await self.conn.fetch("SELECT topic FROM datapoints")
                topics = list(set([datapoint["topic"] for datapoint in datapoints]))
                for topic in topics:
                    await client.unsubscribe(topic)
                    logging.info(f"Unsubscribed from {topic}")
                await self.conn.execute("""DELETE FROM datapoints""")
            else:
                logging.error(f"Unknown command: {command}")
        except Exception as e:
            logging.error(e)
        finally:
            logging.info(f"Done processing command: {command} {topic}")

    async def process_mqtt_message(
        self, topic: str, message: str, session: aiohttp.ClientSession
    ) -> None:
        """
        Processes a single MQTT message.

        Args:
            message (Tuple[str, str, Client]): A tuple containing the topic, the payload, and the MQTT client used by the gateway.
        """
        # Get all datapoints for the topic from the cache
        # If the topic is not in the cache, ask Postgres
        if not await self.cache.hlen(topic):
            logging.info(
                f"No datapoints found for topic {topic} in cache, asking Postgres..."
            )
            datapoints = await self.get_datapoints_by_topic(topic)
            if not datapoints:
                logging.info(
                    f"No datapoints found for topic {topic} in Postgres"
                )
                return
            logging.info(f"Got {len(datapoints)} datapoints from Postgres")
            # Add the datapoints to the cache
            for datapoint in datapoints:
                await self.cache.hset(
                    topic, datapoint["object_id"], json.dumps(datapoint)
                )

        datapoints = await self.cache.hgetall(topic)
        for datapoint in datapoints.values():
            datapoint = json.loads(datapoint.decode("utf-8"))
            # Get the value from the payload using jsonpath
            parsed_result = parse(datapoint["jsonpath"]).find(
                json.loads(message.decode("utf-8"))
            )
            if len(parsed_result) > 0:
                value = parsed_result[0].value
                payload = {
                    datapoint["attribute_name"]: value
                }
                # Send the payload to the Orion Context Broker
                try:
                    await session.patch(
                        url=f"{orion_url}/v2/entities/{datapoint['entity_id']}/attrs?type={datapoint['entity_type']}&options=keyValues",
                        json=payload,
                        # TODO support other headers
                        headers={
                            "fiware-service": service,
                            "fiware-servicepath": service_path,
                        },
                    )
                    logging.info(f"Sent {payload} to Orion Context Broker")
                except Exception as e:
                    logging.error(e)
                    continue
            else:
                logging.warning(
                    f"Can not locate {datapoint['jsonpath']} for topic {topic}")

    async def mqtt_listener(self, client: Client) -> None:
        """
        Listens to MQTT for new messages on subscribed topics. When a message is received, the on_message callback function is called.
        Also subscribes to all topics in the database on startup.
        The callback function is called asynchronously, which means that the listener can continue to listen for new messages while the callback function is being executed.
        This is important because the callback function can take a long time to execute, for example if it needs to query the database.

        Args:
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        logging.info("Listening to MQTT...")
        topics = await self.get_unique_topics()
        logging.info(f"Subscribing to {len(topics)} topics... ({topics})")
        for topic in topics:
            await client.subscribe(topic)
            logging.info(f"Subscribed to topic {topic}")
        async with client.messages() as messages:
            async for message in messages:
                logging.info(f"Receive data {message.payload} from topic {message.topic}")
                self.mqtt_queue.put_nowait(
                    ((str(message.topic), message.payload))
                )

    async def redis_listener(self) -> None:
        """
        Listens to Redis for new messages on subscribed channels. When a message is received, the on_redis_message callback function is called.
        Also subscribes to all channels in the database on startup.
        The callback function is called asynchronously, which means that the listener can continue to listen for new messages while the callback function is being executed.
        """
        stream_name = "manage_topics"
        group_name = "manage_topics_group"
        consumer_name = str(uuid4())

        try:
            await self.notifier.xgroup_create(stream_name, group_name, mkstream=True)
        except Exception as e:
            logging.error(e)
            pass

        logging.info(f"Listening to Stream {stream_name}...")
        while True:
            try:
                async with async_timeout.timeout(1):
                    messages = await self.notifier.xreadgroup(
                        group_name,
                        consumer_name,
                        {stream_name: ">"},
                        count=1,
                    )
                    for message in messages:
                        stream, payload = message
                        message_id, data = payload[0]
                        logging.info(f"Received message {message_id}")
                        logging.info(f"Received data {data}")
                        self.redis_queue.put_nowait(data)
                        await self.notifier.xack(stream_name, group_name, message_id.decode("utf-8"))
            except asyncio.TimeoutError:
                pass
                    
                        # The following methods are used to interact with the Postgres database.
    async def get_datapoints(self):
        """
        Returns a list of all datapoints in the Postgres database.
        """
        async with self.conn.transaction():
            return await self.conn.fetch("SELECT * FROM datapoints")

    async def get_datapoints_by_topic(self, topic: str):
        """
        Returns a list of all datapoints with the given topic in the Postgres database.
        """
        async with self.conn.transaction():
            records = await self.conn.fetch(
                "SELECT object_id, jsonpath, entity_id, entity_type, attribute_name FROM datapoints WHERE topic = $1",
                topic,
            )
            return [dict(record) for record in records]

    async def get_unique_topics(self) -> List[str]:
        """
        Returns a list of all unique topics in the Postgres database.
        """
        async with self.conn.transaction():
            records = await self.conn.fetch("SELECT DISTINCT topic FROM datapoints")
            return [record["topic"] for record in records]

    # End of Postgres methods

    async def run(self):
        """
        Starts the gateway and runs the main loop. Simultaneously listens to PostgreSQL
        for new topics to subscribe or unsubscribe to. In case of a connection error,
        the gateway will try to reconnect after 5 seconds and will continue to do so
        until a connection is established.
        """
        await self.cache.flushdb()
        self.conn = await asyncpg.connect(DATABASE_URL)
        self.s = aiohttp.ClientSession()
        while True:
            reconnect_interval = 5
            try:
                # Client connects to the broker when enter the "with" statement and
                # disconnects when we exit it
                async with Client(
                        hostname=MQTT_HOST,
                        port=MQTT_PORT,
                        username=MQTT_USER,
                        password=MQTT_PASSWORD,
                        tls_context=tls_context
                ) as client:  # only where the mqtt client is connected
                    tasks = [
                        # mqtt listener put the coming mqtt messages to mqtt_queue
                        asyncio.create_task(self.mqtt_listener(client)),
                        # redis listener put the coming API command to redis_queue (or API queue)
                        asyncio.create_task(self.redis_listener()),
                        # workers have two types, mqtt_workers and redis_workers
                        #  mqtt_worker get message from mqtt queue and forward to FIWARE
                        #  redis_workers get the command from redis queue and complete certain job
                        asyncio.create_task(self.start_workers(client)),
                    ]
                    await asyncio.gather(*tasks)
            except MqttError as error:
                logging.error(
                    f"MQTT error: {error} - reconnecting in {reconnect_interval} seconds"
                )
                await asyncio.sleep(reconnect_interval)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    gateway = MqttGateway()
    asyncio.run(gateway.run())
