# Implementing the IoT Agent MQTT Gateway

import paho.mqtt.client as mqtt
import json
import time
import requests
from filip.clients.ngsi_v2 import IoTAClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from uuid import uuid4


from database import PostgresDB
from sensor import Lorawan

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]
orion = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"
iota_7896 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_http_port']}"
iota_4041 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}"
service = config["gateway_setup"]["fiware_service"]
servicepath = config["gateway_setup"]["fiware_servicepath"]
header = FiwareHeader(service=service, service_path=servicepath)

class MqttGateway(IoTAMQTTClient):
    def __init__(self):
        super().__init__(client_id="gateway",
                         protocol=mqtt.MQTTv5)
        
        self.connect(host=mqtt_broker_address)
                         
        s = requests.Session()
        self.iota_client = IoTAClient(url=iota_4041, 
                                      session=s,
                                      fiware_header=header
                                      ) 

        self.database = PostgresDB()

        # create gateway device
        self.gateway_device = Device(
            device_id="gateway:001",
            entity_name="ngsi-ld:urn:Gateway:001",
            entity_type="Gateway",
            protocol="IoTA-JSON")
        
        try:
            self.iota_client.post_device(device=self.gateway_device,
                                         update=False)
        except requests.exceptions.HTTPError as e:
            print(f"Gateway device already exists: {e}")

    def add_datapoint(self, device: Lorawan):
        object_id = str(uuid4())
        print(f"Adding device {device.name} to the gateway")
        self.gateway_device.add_attribute(
            DeviceAttribute(
                object_id=object_id,
                name=object_id
            )
        )
        self.gateway_subscribe(topic=device.topic)
        self.database.add_datapoint(object_id=object_id, jsonpath=f"$..{device.attribute}", topic=device.topic)
        self.iota_client.update_device(device=self.gateway_device)

    def remove_datapoint(self, device: Device):
        print(f"Removing device {device.name} from the gateway")
        self.gateway_device.delete_attribute(
            DeviceAttribute(
                object_id=device.id,
                name = device.name,
            )
        )
        self.database.delete_device(device.id, device.topic)
        self.iota_client.update_device(device=self.gateway_device)
        
    def update_gateway(self, topic, payload):
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
        
    def clean_up(self):
        clear_iot_agent(url=iota_4041, fiware_header=FiwareHeader(service, servicepath))
        clear_context_broker(url=orion, fiware_header=FiwareHeader(service, servicepath))
        
    def run(self):
        self.loop_forever()


if __name__ == "__main__":
    
    sensor = Lorawan('lorawan', 'test/gateway', 'temperature')
    gateway = MqttGateway()
    gateway.add_datapoint(sensor)
    print(gateway.gateway_device.attributes)
