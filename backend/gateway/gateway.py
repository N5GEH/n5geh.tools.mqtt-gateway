"""
This module implements the MQTT IoT Gateway.
"""

import asyncio
import json
import os
from typing import List, Tuple

import aiohttp
import async_timeout
import asyncpg
from aiologger import Logger
from aiologger.handlers.files import AsyncFileHandler
from asyncio_mqtt import Client, MqttError
from filip.models.base import FiwareHeader
from jsonpath_ng import parse
from redis import asyncio as aioredis
from uuid import uuid4

# Load configuration from JSON file
MQTT_HOST = os.environ.get("MQTT_HOST", "localhost")
REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
orion = os.environ.get("ORION_URL", "http://localhost:1026")
service = os.environ.get("FIWARE_SERVICE", "gateway")
servicepath = os.environ.get("FIWARE_SERVICEPATH", "/gateway")
header = FiwareHeader(service=service, service_path=servicepath)
api_key = os.environ.get("API_KEY", "plugnplay")

host = os.environ.get("POSTGRES_HOST", "localhost")
user = os.environ.get("POSTGRES_USER", "karelia")
password = os.environ.get("POSTGRES_PASSWORD", "postgres")
database = os.environ.get("POSTGRES_DB", "iot_devices")

DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"


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
        self.logger = Logger.with_default_handlers(name="mqtt-gateway")
        self.logger.add_handler(AsyncFileHandler("mqtt-gateway.log"))

    async def mqtt_worker(self, client: Client) -> None:
        async with aiohttp.ClientSession() as worker_session:
            async with Client(MQTT_HOST, keepalive=60000) as worker_client:
                while True:
                    try:
                        topic, payload = await self.mqtt_queue.get()
                        await self.process_mqtt_message(topic, payload, worker_client, worker_session)
                        self.mqtt_queue.task_done()
                    except Exception as e:
                        self.logger.error(e)
                        continue

    async def redis_worker(self, client: Client) -> None:
        while True:
            try:
                data = await self.redis_queue.get()
                await self.process_redis_message(data, client=client)
                self.redis_queue.task_done()
            except Exception as e:
                self.logger.error(e)
                continue

    async def start_workers(self, client: Client) -> None:
        mqtt_workers = [asyncio.create_task(self.mqtt_worker(client)) for _ in range(12)]
        redis_workers = [asyncio.create_task(self.redis_worker(client)) for _ in range(4)]
        await asyncio.gather(*(mqtt_workers + redis_workers))

    async def process_redis_message(
        self, message: bytes, client: Client
    ) -> None:
        """
        Processes a single Redis message.

        Args:
            message (Tuple[str, str, Client]): A tuple containing the command, the topic, and the MQTT client used by the gateway.
        """
        decoded_data = {k.decode(): v.decode() for k, v in message.items()}

        command = list(decoded_data.keys())[0]
        topic = list(decoded_data.values())[0]

        try:
            print(f"Processing command: {command} {topic}")
            if command == "subscribe":
                await client.subscribe(topic)
                self.logger.info(f"Subscribed to {topic}")
            elif command == "unsubscribe":
                await client.unsubscribe(topic)
                self.logger.info(f"Unsubscribed from {topic}")
            else:
                self.logger.error(f"Unknown command: {command}")
        except Exception as e:
            self.logger.error(e)
        finally:
            self.logger.info(f"Done processing command: {command} {topic}")

    async def process_mqtt_message(
        self, topic: str, message: str, client: Client, session: aiohttp.ClientSession
    ) -> None:
        """
        Processes a single MQTT message.

        Args:
            message (Tuple[str, str, Client]): A tuple containing the topic, the payload, and the MQTT client used by the gateway.
        """
        # Get all datapoints for the topic from the cache
        # If the topic is not in the cache, ask Postgres
        if not await self.cache.hlen(topic):
            await self.logger.info(
                f"No datapoints found for topic {topic} in cache, asking Postgres..."
            )
            datapoints = await self.get_datapoints_by_topic(topic)
            if not datapoints:
                await self.logger.info(
                    f"No datapoints found for topic {topic} in Postgres"
                )
                return
            await self.logger.info(f"Got {len(datapoints)} datapoints from Postgres")
            # Add the datapoints to the cache
            for datapoint in datapoints:
                await self.cache.hset(
                    topic, datapoint["object_id"], json.dumps(datapoint)
                )

        datapoints = await self.cache.hgetall(topic)
        for datapoint in datapoints.values():
            datapoint = json.loads(datapoint.decode("utf-8"))
            # Get the value from the payload using jsonpath
            value = (
                parse(datapoint["jsonpath"])
                .find(json.loads(message.decode("utf-8")))[0]
                .value
            )
            if value:
                payload = {
                    datapoint["attribute_name"]: {
                        "type": "Number",
                        "value": value,
                    }
                }
                # Send the payload to the Orion Context Broker
                try:
                    await session.patch(
                        url=f"{orion}/v2/entities/{datapoint['entity_id']}/attrs?type={datapoint['entity_type']}",
                        json=payload,
                        headers={
                            "fiware-service": header.service,
                            "fiware-servicepath": header.service_path,
                        },
                    )
                    await self.logger.info(f"Sent {payload} to Orion Context Broker")
                except Exception as e:
                    await self.logger.error(e)
                    continue

    async def mqtt_listener(self, client: Client) -> None:
        """
        Listens to MQTT for new messages on subscribed topics. When a message is received, the on_message callback function is called.
        Also subscribes to all topics in the database on startup.
        The callback function is called asynchronously, which means that the listener can continue to listen for new messages while the callback function is being executed.
        This is important because the callback function can take a long time to execute, for example if it needs to query the database.

        Args:
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        print("Listening to MQTT...")
        topics = await self.get_unique_topics()
        print(f"Subscribing to {len(topics)} topics... ({topics})")
        for topic in topics:
            await client.subscribe(topic)
            print(f"Subscribed to topic {topic}")
        async with client.messages() as messages:
            async for message in messages:
                self.mqtt_queue.put_nowait(
                    ((str(message.topic), message.payload))
                )

    async def redis_listener(self, client: Client) -> None:
        """
        Listens to Redis for new messages on subscribed channels. When a message is received, the on_redis_message callback function is called.
        Also subscribes to all channels in the database on startup.
        The callback function is called asynchronously, which means that the listener can continue to listen for new messages while the callback function is being executed.

        Args:
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        stream_name = "manage_topics"
        group_name = "manage_topics_group"
        consumer_name = str(uuid4())

        try:
            await self.notifier.xgroup_create(stream_name, group_name, mkstream=True)
        except Exception as e:
            print(e)
            pass

        print(f"Listening to Stream {stream_name}...")
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
                        print(f"Received message {message_id}")
                        print(f"Received data {data}")
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
        Starts the gateway and runs the main loop. Simultaneously listens to PostgreSQL for new topics to subscribe or unsubscribe to.
        In case of a connection error, the gateway will try to reconnect after 5 seconds and will continue to do so until a connection is established.
        """
        await self.cache.flushdb()
        self.conn = await asyncpg.connect(DATABASE_URL)
        self.s = aiohttp.ClientSession()
        while True:
            reconnect_interval = 5
            try:
                async with Client(hostname=MQTT_HOST) as client:
                    tasks = [
                        asyncio.create_task(self.mqtt_listener(client)),
                        asyncio.create_task(self.redis_listener(client)),
                        asyncio.create_task(self.start_workers(client)),
                    ]
                    await asyncio.gather(*tasks)
            except MqttError as error:
                print(
                    f"MQTT error: {error} - reconnecting in {reconnect_interval} seconds"
                )
                await asyncio.sleep(reconnect_interval)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    gateway = MqttGateway()
    asyncio.run(gateway.run())
