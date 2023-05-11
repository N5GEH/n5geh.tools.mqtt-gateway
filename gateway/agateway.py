import json
from threading import Thread
from uuid import uuid4

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

import asyncio
import asyncpg

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

# Database connection settings
DATABASE_URL = f"postgres://{user}:{password}@{host}:5432/{database}"

class MqttGateway(IoTAMQTTClient):
    def __init__(self):
        super().__init__(client_id="gateway", protocol=mqtt.MQTTv5)

        self.connect(host=mqtt_broker_address)

        self.s = requests.Session()
        self.iota_client = IoTAClient(url=iota_4041, session=self.s, fiware_header=header)
        self.database = PostgresDB()

        # Setting up Redis pubsub for adding and removing datapoints

        # Create gateway device
        self.gateway_device = Device(
            device_id="gateway:001",
            entity_name="ngsi-ld:urn:Gateway:001",
            entity_type="Gateway",
            protocol="IoTA-JSON",
        )
        
        initial_topics = []
        # Subscribe to all topics from the database
        for object_id, jsonpath, topic in self.database.get_all_datapoints():
            self.add_datapoint(
                object_id=object_id, 
                jsonpath=jsonpath, 
                topic=topic, 
                subscribe=True if topic not in initial_topics else False
            )
            initial_topics.append(topic) if topic not in initial_topics else None
        try:
            self.iota_client.post_device(device=self.gateway_device, update=False)
        except requests.exceptions.HTTPError as e:
            print(f"Gateway device already exists: {e}")

    async def postgres_listener(self):
        """
        Listens to Postgres for new topics to subscribe or unsubscribe to.
        """
        conn = await asyncpg.connect(DATABASE_URL)
        await conn.add_listener("add_datapoint", self.process_pg_notification)
        await conn.add_listener("remove_datapoint", self.process_pg_notification)
        while True:
            await asyncio.sleep(1)
          
    def on_postgres_notify(self, connection, pid, channel, payload):
        """
        Callback function that processes incoming PostgreSQL notifications.

        Args:
            connection (asyncpg.Connection): The PostgreSQL connection instance.
            pid (int): The process ID of the notifying backend.
            channel (str): The channel name on which the notification was sent.
            payload (str): The notification payload.
        """
        print(f"Received notification on channel '{channel}' with payload '{payload}'")
        message = json.loads(payload)

        if channel == "add_datapoint":
            self.add_datapoint(
                object_id=message["object_id"],
                jsonpath=message["jsonpath"],
                topic=message["topic"],
                subscribe=message["subscribe"],
            )

        elif channel == "remove_datapoint":
            self.remove_datapoint(
                object_id=message["object_id"],
                jsonpath=message["jsonpath"],
                topic=message["topic"],
                unsubscribe=message["unsubscribe"],
            )

