"""
This module implements the IoT Agent MQTT Gateway.
"""

import json
from threading import Thread
from uuid import uuid4

import paho.mqtt.client as mqtt
import redis
import requests
from database import PostgresDB
from filip.clients.mqtt import IoTAMQTTClient
from filip.clients.ngsi_v2 import IoTAClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from jsonpath_ng import parse
from paho.mqtt.subscribeoptions import SubscribeOptions

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

class MqttGateway(IoTAMQTTClient):
    def __init__(self):
        super().__init__(client_id="gateway", protocol=mqtt.MQTTv5)

        self.connect(host=mqtt_broker_address)

        self.s = requests.Session()
        self.iota_client = IoTAClient(url=iota_4041, session=self.s, fiware_header=header)
        self.database = PostgresDB()

        # Setting up Redis pubsub for adding and removing datapoints
        self.redis_client = redis.Redis(
            host=config["connection_settings"]["server_ip"], port=6379, db=0
        )
        self.pubsub = self.redis_client.pubsub()
        self.pubsub.subscribe("add_datapoint")
        self.pubsub.subscribe("remove_datapoint")

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
        self.gateway_device.add_attribute(
            DeviceAttribute(object_id=object_id, name=object_id)
        )
        self.gateway_subscribe(topic=topic) if subscribe else None
        self.iota_client.update_device(device=self.gateway_device)

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
        self.gateway_device.delete_attribute(DeviceAttribute(object_id=object_id, name=object_id))
        self.gateway_unsubscribe(topic=topic) if unsubscribe else None
        self.iota_client.update_device(device=self.gateway_device)

    def on_message(self, client: mqtt.Client, userdata, message: mqtt.MQTTMessage):
        """
        Callback function that processes incoming MQTT messages.

        Args:
            client (mqtt.Client): The MQTT client instance.
            userdata: User-defined data passed to the callback.
            message (mqtt.MQTTMessage): The received MQTT message.
        """
        print(f"Received message on topic '{message.topic}'")
        datapoints = self.database.get_datapoint(topic=message.topic)
        if not datapoints:
            print(f"No datapoint found for topic {message.topic}")
            return
        for datapoint in datapoints:
            object_id, jsonpath = datapoint
            data = parse(jsonpath).find(json.loads(message.payload))
            if data:
                print(f"I will be sending <{object_id}: {data[0].value}> to the IoT Agent")
                #request = self.s.post(
                #    f"{iota_7896}/iot/json?k={api_key}&i={object_id}",
                #    headers={"Content-Type": "application/json"},
                #    data=json.dumps({object_id: data[0].value}),
                #)
                #print(request.text)

    def update_gateway(self, topic: str, payload: str):
        """
        Updates the gateway based on the given topic and payload.

        Args:
            topic (str): The topic associated with the update.
            payload (str): The payload containing the update information.
        """
        device = self.database.get_device_by_topic(topic)
        if device:
            print(f"Updating device {device.id}")
            update_gateway = self.s.post(
                f"{iota_7896}/iot/d?k={device.device_id}&i={device.entity_name}",
                data=payload,
                headers=header,
            )
            print(update_gateway.text)
        else:
            print(f"Device not found for topic {topic}")

    def gateway_subscribe(self, topic: str):
        """
        Subscribes the gateway to a given topic.

        Args:
            topic (str): The topic to subscribe to.
        """
        print(f"Subscribing to topic {topic}")
        self.subscribe(topic=(topic, SubscribeOptions(qos=0)))

    def gateway_unsubscribe(self, topic: str):
        """
        Unsubscribes the gateway from a given topic.

        Args:
            topic (str): The topic to unsubscribe from.
        """
        print(f"Unsubscribing from topic {topic}")
        self.unsubscribe(topic=topic)

    def clean_up(self):
        """
        Cleans up the gateway by clearing the IoT agent and context broker.
        """
        clear_iot_agent(url=iota_4041, fiware_header=FiwareHeader(service, servicepath))
        clear_context_broker(
            url=orion, fiware_header=FiwareHeader(service, servicepath)
        )

    def redis_listener(self):
        """
        Listens to Redis for new topics to subscribe or unsubscribe to.
        """
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                if message['channel'] == b'add_datapoint':
                    data = json.loads(message['data'].decode('utf-8'))
                    print(data)
                    self.add_datapoint(
                        object_id=data['object_id'],
                        jsonpath=data['jsonpath'],
                        topic=data['topic'],
                        subscribe=data['subscribe']
                    )
                if message['channel'] == b'remove_datapoint':
                    data = json.loads(message['data'].decode('utf-8'))
                    self.remove_datapoint(
                        object_id=data['object_id'],
                        topic=data['topic'],
                        jsonpath=data['jsonpath'],
                        unsubscribe=data['unsubscribe']
                    )

    def run(self):
        """
        Starts the gateway and runs the main loop.
        Simultaneously listens to Redis for new topics to subscribe or unsubscribe to.
        """
        t1 = Thread(target=self.loop_forever)
        t2 = Thread(target=self.redis_listener)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == "__main__":
    gateway = MqttGateway()
    gateway.run()
           
