# Implementing the IoT Agent MQTT Gateway

import json
from uuid import uuid4

import paho.mqtt.client as mqtt
import requests
from database import PostgresDB
from filip.clients.mqtt import IoTAMQTTClient
from filip.clients.ngsi_v2 import IoTAClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from jsonpath_ng import parse
from sensor import Lorawan
from threading import Thread

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]
orion = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"
iota_7896 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_http_port']}"
iota_4041 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}"
service = config["gateway_setup"]["fiware_service"]
servicepath = config["gateway_setup"]["fiware_servicepath"]
header = FiwareHeader(service=service, service_path=servicepath)

# apparently this needs to be saved as a static function/class method to be used as a callback
class MqttGateway(IoTAMQTTClient):
    def __init__(self):
        super().__init__(client_id="gateway", protocol=mqtt.MQTTv5)

        self.connect(host=mqtt_broker_address)

        s = requests.Session()
        self.iota_client = IoTAClient(url=iota_4041, session=s, fiware_header=header)

        self.database = PostgresDB()

        # create gateway device
        self.gateway_device = Device(
            device_id="gateway:001",
            entity_name="ngsi-ld:urn:Gateway:001",
            entity_type="Gateway",
            protocol="IoTA-JSON",
        )

        try:
            self.iota_client.post_device(device=self.gateway_device, update=False)
        except requests.exceptions.HTTPError as e:
            print(f"Gateway device already exists: {e}")

    def add_datapoint(self, topic: str, attribute: str):
        object_id = str(uuid4())
        print(
            f"Adding datapoint {object_id} with attribute {attribute} and topic {topic} to the gateway"
        )
        self.gateway_device.add_attribute(
            DeviceAttribute(object_id=object_id, name=object_id)
        )
        self.gateway_subscribe(topic=topic)
        self.database.add_datapoint(
            object_id=object_id, jsonpath=f"$..{attribute}", topic=topic
        )
        return object_id
        # self.iota_client.update_device(device=self.gateway_device)

    def on_message(self, client: mqtt.Client, userdata, message: mqtt.MQTTMessage):
        print(
            f"Received message on topic '{message.topic}'"
        )
        datapoints = self.database.get_datapoint(topic=message.topic)
        print(datapoints)
        if not datapoints:
            print(f"No datapoint found for topic {message.topic}")
            return
        for datapoint in datapoints:
            object_id, jsonpath = datapoint
            data = parse(jsonpath).find(json.loads(message.payload))
            if data:
                print(f"I would be sending {object_id}: {data[0].value}")
                
        
    def remove_datapoint(self, topic: str, attribute: str):
        print(
            f"Removing datapoint with attribute {attribute} and topic {topic} from the gateway"
        )
        id = self.database.get_object_id(topic=topic, attribute=attribute)
        self.gateway_device.delete_attribute(DeviceAttribute(object_id=id, name=id))
        self.database.delete_device(id, topic)
        self.iota_client.update_device(device=self.gateway_device)

    def update_gateway(self, topic: str, payload: str):
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

    def gateway_subscribe(self, topic):
        if not self.database.check_topic(topic):
            self.subscribe(topic)
        else:
            print(f"Already subscribed to {topic}")
            self.subscribe(
                topic
            )  # TODO: subscribing for now anyway, but should be removed later

    def clean_up(self):
        clear_iot_agent(url=iota_4041, fiware_header=FiwareHeader(service, servicepath))
        clear_context_broker(
            url=orion, fiware_header=FiwareHeader(service, servicepath)
        )

    def run(self):
        
        t1 = Thread(target=self.loop_forever)
        
        def t2():
            while True:
                topic = shared_queue.get()
                print(f"Subscribing to {topic}")
                self.gateway_subscribe(topic)
                shared_queue.task_done()
        
        t2 = Thread(target=t2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == "__main__":
    gateway = MqttGateway()
    gateway.run()