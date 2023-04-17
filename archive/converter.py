from paho.mqtt.client import Client, MQTT_CLEAN_START_FIRST_ONLY, MQTTMessage
from paho.mqtt.client import MQTTv5
from typing import List
import time
import json
import threading
import pandas as pd
from filip.clients.mqtt.client import IoTAMQTTClient
from model import Topic
from filip.models.ngsi_v2.iot import DeviceAttribute
from iota_gateway import MqttGateway

# Settings
API_KEY = "plugnplay"
GATEWAY_ID = "gateway:001"
HOST = "161.35.205.102"
PORT = 1883

# invalid characters
# TODO maybe useful
chars_invalid = [
    "*", "#", "+", ":", "-", "/", "?", "&", "^"
]


class TopicConverter:

    def __init__(self, topic: str, gateway: MqttGateway, **kwargs):
        super().__init__(**kwargs)
        # TODO give TopicConverter the access to gateway?
        self.gateway = gateway

        # TODO Read the all parameters from environment? or from gateway object?
        self.apikey = API_KEY
        self.gateway_id = GATEWAY_ID
        self.host = HOST
        self.port = PORT

        # TODO use the model to initialize the topic and sensor attribute
        self.topic = Topic(topic_name=topic)

        # initialize the MQTT client
        self.mqtt_client = Client(protocol=MQTTv5)
        self.mqtt_client.on_message = self.on_message

    def check_attribute(self, attribute_name):
        """
        Check if the attribute already exist, otherwise this function create this attribute
        on FIWARE

        Args:
            attribute_name:

        Returns:

        """
        # TODO if the auto provision of attribute works, we dont need this anymore
        # TODO maybe use another list to check more efficiently
        for attribute in self.topic.attributes:
            if attribute.name == attribute_name:
                break
        else:
            # new attribute
            # TODO leave object_id blank
            new_attribute = DeviceAttribute(
                name=attribute_name,
                type="Number",  # TODO hard coded, must be changed later. Maybe check the value,
                # TODO the object id is now empty
            )
            # TODO where to store the updated time?
            self.topic.attributes.append(new_attribute)

            # TODO
            #  create new attribute in gateway
            self.gateway.register_attribute(new_attribute)

            print(f"create new attribute: {attribute_name}", flush=True)

    def convert_message(self, msg: MQTTMessage):
        """
        Convert one mqtt message to FIWARE specific format
        :return: topic, payload
        """
        payload = msg.payload.decode('utf-8')
        topic = msg.topic

        payload_dict: dict = json.loads(payload)

        # TODO current convention:
        #  1. / is replaced with __
        #  2. use ___ to separate old topic and the attribute name
        topic_fix = topic.replace("/", "__")
        topic_fix = replace_special_char(topic_fix, rpl="_")

        # TODO right now only support single level attributes. should be capable to deal with deeper payload
        new_payload_dict = {f"{topic_fix}___{replace_special_char(attr_name, rpl='_')}": payload_dict[attr_name]
                            for attr_name in payload_dict}

        # check if there is new attributes
        for attr_name in new_payload_dict:
            print(f"check attribute: {attr_name}", flush=True)
            self.check_attribute(attr_name)

        new_payload = json.dumps(new_payload_dict)

        new_topic = f"/json/{self.apikey}/{self.gateway_id}/attrs"
        return new_topic, new_payload

    def on_message(self, client: Client, obj, msg: MQTTMessage):
        new_topic, new_payload = self.convert_message(msg)
        print(f"convert to topic: {new_topic},\npayload: {new_payload}", flush=True)
        client.publish(new_topic, new_payload)

    def run(self):
        self.mqtt_client.connect(host=self.host,
                                 port=self.port,
                                 keepalive=60,
                                 bind_address="",
                                 bind_port=0,
                                 clean_start=MQTT_CLEAN_START_FIRST_ONLY,
                                 properties=None)
        self.mqtt_client.subscribe(topic=self.topic.topic_name)
        self.mqtt_client.loop_start()
        while True:
            time.sleep(0.5)  # TODO what is the best sleep time
            print("Mqtt loop")


def replace_special_char(text, rpl: str = "_", ignore: str = ""):
    text_new = "".join(char if char.isalnum() or char == ignore else rpl for char in text)
    return text_new


def add_new_client(*args):
    mqtt_converter = TopicConverter(*args)
    mqtt_converter.run()


def add_topic(topic: str, *arg):
    """Create a new client for the topic"""
    # TODO use name to identify the object?
    t = threading.Thread(target=add_new_client, daemon=True, name=topic, args=(topic, *arg))
    t.start()
