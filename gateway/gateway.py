"""
This module implements the MQTT IoT Gateway.
"""

import json
import paho.mqtt.client as mqtt
import requests
from adatabase import PostgresDB
from filip.clients.mqtt import IoTAMQTTClient
from filip.clients.ngsi_v2 import IoTAClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from jsonpath_ng import parse
from paho.mqtt.subscribeoptions import SubscribeOptions
import asyncpg
import asyncio
from asyncio_mqtt import Client, MqttError

# Load configuration from JSON file
config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]
orion = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"
iota_7896 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_http_port']}"
iota_4041 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}"
service = config["gateway_setup"]["fiware_service"]
servicepath = config["gateway_setup"]["fiware_servicepath"]
header = FiwareHeader(service=service, service_path=servicepath)
api_key = config["gateway_setup"]["api_key"]

host = config["postgres_setup"]["host"]
user = config["postgres_setup"]["user"]
password = config["postgres_setup"]["password"]
database = config["postgres_setup"]["database"]

DATABASE_URL = f"postgres://{user}:{password}@{host}:5432/{database}"

class MqttGateway(Client):
    def __init__(self):
        super().__init__(hostname=mqtt_broker_address, client_id="gateway", protocol=mqtt.MQTTv5)
        self.s = requests.Session()
        # Create gateway device
        self.gateway_device = Device(
            device_id="gateway:001",
            entity_name="ngsi-ld:urn:Gateway:001",
            entity_type="Gateway",
            protocol="IoTA-JSON",
        )        
        self.iota_client = IoTAClient(url=iota_4041, session=self.s, fiware_header=header)
        try:
            self.iota_client.post_device(device=self.gateway_device, update=False)
        except requests.exceptions.HTTPError as e:
            print(f"Gateway device already exists: {e}")

            
    def add_datapoint(self, object_id: str, jsonpath: str, topic: str, subscribe: bool) -> None:
        """
        Adds a new datapoint to the gateway.

        Args:
            object_id (str): The object ID of the datapoint.
            topic (str): The topic to which the datapoint should be added.
            attribute (str): The attribute associated with the datapoint.

        Returns:
            str: The UUID of the created datapoint.
        """
        print(
            f"Adding datapoint {object_id} with jsonpath {jsonpath} and topic {topic} to the gateway"
        )

    def remove_datapoint(self, object_id: str, jsonpath: str, topic: str, unsubscribe: bool) -> None:
        """
        Removes a datapoint from the gateway.

        Args:
            topic (str): The topic associated with the datapoint to be removed.
            attribute (str): The attribute associated with the datapoint to be removed.
            unsubscribe (bool): Whether the gateway should unsubscribe from the topic.
        """
        print(
            f"Removing datapoint with jsonpath {jsonpath} and topic {topic} from the gateway"
        )

    async def on_message(self, topic, payload):
        print(f"Received message on topic '{topic}'")
        datapoints = await self.database.get_datapoint(topic=topic)
        if not datapoints:
            print(f"No datapoint found for topic {topic}")
            return
        for datapoint in datapoints:
            object_id, jsonpath = datapoint
            data = parse(jsonpath).find(json.loads(payload))
            if data:
                print(f"I will be sending <{object_id}: {data[0].value}> to the IoT Agent")

    async def mqtt_listener(self):
        async with PostgresDB() as database:
            async with Client(mqtt_broker_address) as client:
                for object_id, jsonpath, topic in await database.get_all_datapoints():
                    await client.subscribe(topic)
                    print(f"Subscribed to topic {topic}")
                async with client.messages() as messages:
                    async for message in messages:
                        payload = message.payload.decode()
                        topic = message.topic
                        await self.on_message(topic=topic, payload=payload)
    
    async def postgres_listener(self):
        """
        Listens to PostgreSQL for new topics to subscribe or unsubscribe to.
        """
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.add_listener("add_datapoint", self.on_postgres_notification)
        await conn.add_listener("remove_datapoint", self.on_postgres_notification)
        
        while True:
            await asyncio.sleep(1)  # keeps the connection alive
        
    def on_postgres_notification(self, conn: asyncpg.Connection, pid: int, channel: str, payload: str):
        """
        Callback function that processes PostgreSQL notifications.
        
        Args:
            conn (asyncpg.Connection): The connection that received the notification.
            pid (int): The process ID of the connection that received the notification.
            channel (str): The name of the channel that received the notification.
            payload (str): The payload of the notification.
        """
        print(f"Received notification on channel '{channel}'")
        if channel == "add_datapoint":
            self.add_datapoint(**json.loads(payload))
        elif channel == "remove_datapoint":
            self.remove_datapoint(**json.loads(payload))
                
    async def run(self):
        """
        Starts the gateway and runs the main loop.
        Simultaneously listens to Postgres for new topics to subscribe or unsubscribe to.
        """
        tasks = [self.mqtt_listener(), self.postgres_listener()]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    gateway = MqttGateway()
    asyncio.run(gateway.run())
