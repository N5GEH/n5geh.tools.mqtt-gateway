"""
This module implements the MQTT IoT Gateway.
"""

import json
import paho.mqtt.client as mqtt
import requests
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.context import ContextAttribute
from filip.clients.ngsi_v2 import ContextBrokerClient
from filip.models.ngsi_v2.iot import Device, DeviceAttribute
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from jsonpath_ng import parse
import asyncpg
import asyncio
from asyncio_mqtt import Client, MqttError, Topic
import functools
import time
import os
from redis import asyncio as aioredis
from typing import List

# Load configuration from JSON file
MQTT_HOST = os.environ.get("MQTT_HOST", "localhost")
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
orion = os.environ.get("ORION_URL", "http://localhost:1026")
service = os.environ.get("FIWARE_SERVICE", "mqtt_gateway")
servicepath = os.environ.get("FIWARE_SERVICEPATH", "/mqttgateway")
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
        super().__init__(hostname=MQTT_HOST, client_id="gateway", protocol=mqtt.MQTTv5)
        self.s = requests.Session()
        # Create gateway device
        self.gateway_device = Device(
            device_id="gateway:001",
            entity_name="ngsi-ld:urn:Gateway:001",
            entity_type="Gateway",
            protocol="IoTA-JSON",
        )        
        self.orion = ContextBrokerClient(url=orion, headers=header)
        self.cache = aioredis.from_url(f"redis://{REDIS_HOST}")
        self.conn = None  # Initialized in run()
            
    async def add_datapoint(self, object_id: str, jsonpath: str, topic: str, entity_id: str, entity_type: str, attribute_name: str, subscribe: bool, client: Client) -> None:
        """
        Adds a new datapoint to the gateway.

        Args:
            object_id (str): The object ID of the datapoint.
            jsonpath (str): The jsonpath of the attribute.
            topic (str): The topic to which the datapoint should be added.
            entity_id (str): The entity ID of the datapoint in the Orion Context Broker.
            entity_type (str): The entity type of the datapoint in the Orion Context Broker.
            attribute_name (str): The attribute name of the datapoint in the Orion Context Broker.
            subscribe (bool): Whether the gateway should subscribe to the topic.
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        print(
            f"Adding datapoint {object_id} with jsonpath {jsonpath} and topic {topic} to the gateway"
        )
        await client.subscribe(topic) if subscribe else None
        await self.cache.sadd(topic, json.dumps({"object_id": object_id,
                                      "jsonpath": jsonpath,
                                      "entity_id": entity_id,
                                      "entity_type": entity_type,
                                      "attribute_name": attribute_name}))
        print(f"Cache updated, now contains {await self.cache.smembers(topic)}")

    async def remove_datapoint(self, object_id: str, jsonpath: str, topic: str, entity_id: str, entity_type: str, attribute_name: str, unsubscribe: bool, client: Client) -> None:
        """
        Removes a datapoint from the gateway.

        Args:
            object_id (str): The object ID of the datapoint.
            jsonpath (str): The jsonpath of the attribute.
            topic (str): The topic to which the datapoint should be added.
            entity_id (str): The entity ID of the datapoint in the Orion Context Broker.
            entity_type (str): The entity type of the datapoint in the Orion Context Broker.
            attribute_name (str): The attribute name of the datapoint in the Orion Context Broker.
            unsubscribe (bool): Whether the gateway should unsubscribe to the topic.
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        print(
            f"Removing datapoint with jsonpath {jsonpath} and topic {topic} from the gateway"
        )
        await client.unsubscribe(topic) if unsubscribe else None
        await self.cache.srem(topic, json.dumps({"object_id": object_id,
                                        "jsonpath": jsonpath,
                                        "entity_id": entity_id,
                                        "entity_type": entity_type,
                                        "attribute_name": attribute_name}))
        print(f"Cache updated, {topic} now contains {await self.cache.smembers(topic)}")
        await self.cache.delete(topic) if not await self.cache.smembers(topic) else None # Delete topic from cache if it is empty

    async def on_message(self, topic: Topic, payload: str) -> None:
        """
        Callback function that processes MQTT messages. 
        It is called whenever a message is received on a subscribed topic.
        Queries the database for the datapoint associated with the topic containing the jsonpath of the attribute.
        If a datapoint is found, the jsonpath is used to extract the value from the payload, which is then sent to the Orion Context Broker.
        
        Args:
            topic (Topic): The topic on which the message was received. The Topic object is from the asyncio_mqtt library.
            payload (str): The payload of the message.
        """
        start_time = time.time()
        topic = str(topic)  # Convert Topic object to string for easier processing
        print(f"Received message on topic '{topic}'")
        datapoints = await self.cache.smembers(topic)
        if not datapoints:
            print(f"No datapoints found for topic {topic} in cache, asking Postgres...")
            async with PostgresDB(DATABASE_URL) as database:
                datapoints = await database.get_datapoints(topic=topic)
                if not datapoints:
                    print(f"No datapoints found for topic {topic}, ignoring message...")
                    return
                print(f"Succesfully retrieved datapoints for topic {topic} from Postgres: {datapoints}, adding to cache...")
                await self.cache.sadd(topic, *datapoints)
        print(f"Found the following datapoints for topic {topic}: {datapoints}")
        attr_dict = {}
        for datapoint in datapoints:
            datapoint = json.loads(datapoint)
            print(f"Processing datapoint {datapoint['object_id']}...")
            data = parse(datapoint["jsonpath"]).find(json.loads(payload))
            if data and datapoint["entity_id"] and datapoint["entity_type"] and datapoint["attribute_name"]:
                attr_data = {"value": data[0].value}  # type automatically changed to Text, change later?
                attr_dict[datapoint["attribute_name"]] = ContextAttribute(**attr_data)
            if attr_dict:
                print(f"In the end, I will be sending the following data to the Context Broker: {attr_dict}")
                try:
                    self.orion.update_existing_entity_attributes(
                        entity_id=datapoint["entity_id"],
                        entity_type=datapoint["entity_type"],
                        attrs=attr_dict)
                except requests.exceptions.HTTPError as e:
                    print(f"Error while sending data to the Context Broker: {e}")
                finally:
                    print(f"Sent the data to Orion in {time.time() - start_time}")

    async def mqtt_listener(self, client: Client) -> None:
        """
        Listens to MQTT for new messages on subscribed topics. When a message is received, the on_message callback function is called.
        Also subscribes to all topics in the database on startup.
        The callback function is called asynchronously, which means that the listener can continue to listen for new messages while the callback function is being executed.
        This is important because the callback function can take a long time to execute, for example if it needs to query the database.

        Args:
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        topics = await self.get_unique_topics()
        for topic in topics:
            real_topic = str(topic).split("'")[1]
            print(f"Subscribing to topic {real_topic}")
            await client.subscribe(real_topic)
            print(f"Subscribed to topic {real_topic}")
        async with client.messages() as messages:
            async for message in messages:
                payload = message.payload.decode()
                topic = message.topic
                await self.on_message(topic=topic, payload=payload)
    
    async def postgres_listener(self, client):
        """
        Listens to PostgreSQL for new topics to subscribe or unsubscribe to. 
        When a new topic is added or removed from the database, the on_postgres_notification callback function is called.
        The callback function is called asynchronously, which means that the listener can continue to listen for new topics while the callback function is being executed.
        This is important because the callback function can take a long time to execute, for example if it needs to query the database.
        The functools.partial function is used to pass the MQTT client to the callback function, which has a different signature than the callback function expected by the asyncpg library.
        
        Args:
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        conn = await asyncpg.connect(DATABASE_URL)
        on_postgres_notification_with_client = functools.partial(self.on_postgres_notification, client=client)  # pass the MQTT client to the callback function
        await conn.add_listener("add_datapoint", on_postgres_notification_with_client)
        await conn.add_listener("remove_datapoint", on_postgres_notification_with_client)
        
        while True:
            await asyncio.sleep(1)  # keeps the connection alive
        
    async def on_postgres_notification(self, conn: asyncpg.Connection, pid: int, channel: str, payload: str, client: Client) -> None:
        """
        Callback function that processes PostgreSQL notifications.
        It is called whenever a new topic is added or removed from the database.
        
        Args:
            conn (asyncpg.Connection): The connection to the database.
            pid (int): The process ID of the PostgreSQL server process that sent the notification. I shall probably not use this but the signature of the callback function requires it.
            channel (str): The name of the channel that the notification was sent on.
            payload (str): The payload of the notification.
            client (Client): The MQTT client used by the gateway. The Client object is from the asyncio_mqtt library.
        """
        print(f"Received notification on channel '{channel}' with payload '{payload}'")
        if channel == "add_datapoint":
            data = json.loads(payload)
            await self.add_datapoint(object_id=data["object_id"], 
                                        jsonpath=data["jsonpath"], 
                                        topic=data["topic"], 
                                        entity_id=data["entity_id"],
                                        entity_type=data["entity_type"],
                                        attribute_name=data["attribute_name"],
                                        subscribe=data["subscribe"],
                                        client=client)
        elif channel == "remove_datapoint":
            data = json.loads(payload)
            await self.remove_datapoint(object_id=data["object_id"], 
                                        jsonpath=data["jsonpath"], 
                                        topic=data["topic"],
                                        entity_id=data["entity_id"],
                                        entity_type=data["entity_type"],
                                        attribute_name=data["attribute_name"], 
                                        unsubscribe=data["unsubscribe"],
                                        client=client)
        else:
            print(f"Received notification on unknown channel '{channel}'")

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
            return await self.conn.fetch("SELECT object_id, jsonpath, entity_id, entity_type, attribute_name FROM datapoints WHERE topic = $1", topic)
    
    async def get_unique_topics(self) -> List[str]:
        """
        Returns a list of all unique topics in the Postgres database.
        """
        async with self.conn.transaction():
            return await self.conn.fetch("SELECT DISTINCT topic FROM datapoints")
    # End of Postgres methods
    
    async def renew_cache(self):
        """
        This method is called periodically to renew the Redis cache of the gateway.
        """
            
    async def run(self):
        """
        Starts the gateway and runs the main loop. Simultaneously listens to PostgreSQL for new topics to subscribe or unsubscribe to.
        In case of a connection error, the gateway will try to reconnect after 5 seconds and will continue to do so until a connection is established.
        """
        await self.cache.flushall()
        self.conn = await asyncpg.connect(DATABASE_URL)
        while True:
            reconnect_interval = 5
            try:
                async with Client(hostname=MQTT_HOST, client_id="gateway", protocol=mqtt.MQTTv5) as client:
                    tasks = [self.mqtt_listener(client), self.postgres_listener(client)]
                    await asyncio.gather(*tasks)
            except MqttError as error:
                print(f"MQTT error: {error} - reconnecting in {reconnect_interval} seconds")
                await asyncio.sleep(reconnect_interval)
            

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    gateway = MqttGateway()
    asyncio.run(gateway.run())
