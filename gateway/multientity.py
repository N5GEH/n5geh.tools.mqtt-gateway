# testing out the multientity plugin

import paho.mqtt.client as mqtt
import json
import time
import requests
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_context_broker, clear_iot_agent

from database import PostgresDB

config = json.load(open("config.json"))
orion = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"
iota_7896 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_http_port']}"
iota_4041 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}"
service = config["gateway_setup"]["fiware_service"]
servicepath = config["gateway_setup"]["fiware_servicepath"]
header = FiwareHeader(service=service, service_path=servicepath)

class MqttGateway:
    def __init__(self):
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

    def add_device(self, device: Device):
        print(f"Adding device {device.device_id} to the gateway")
        self.gateway_device.add_attribute(
            DeviceAttribute(
                object_id=device.device_id,
                name=device.entity_name,
                type="Number",
                entity_name=f"urn:ngsi-ld:{device.entity_name}",
                entity_type=device.entity_type,
            )
        )
        self.database.add_device(device.device_id, device.entity_name)
        self.iota_client.update_device(device=self.gateway_device)

    def remove_device(self, device: Device):
        print(f"Removing device {device.device_id} from the gateway")
        self.gateway_device.delete_attribute(
            DeviceAttribute(
                object_id=device.device_id,
                name=device.entity_name,
                type="Number",
                entity_name=f"urn:ngsi-ld:{device.entity_name}",
                entity_type=device.entity_type,
            )
        )
        self.database.delete_device(device.device_id)
        self.iota_client.update_device(device=self.gateway_device)
        
    def update_device(self, topic, payload):
        device = self.database.get_device_by_topic(topic)
        if device:
            print(f"Updating device {device.device_id}")
            update_device = self.s.post(
                f"{iota_7896}/iot/d?k={device.device_id}&i={device.entity_name}",
                data=payload,
                headers=header,
            )
            print(update_device.text)
        else:
            print(f"Device not found for topic {topic}")    
        
    def clean_up(self):
        clear_iot_agent(url=iota_4041, fiware_header=FiwareHeader(service, servicepath))
        clear_context_broker(url=orion, fiware_header=FiwareHeader(service, servicepath))


if __name__ == "__main__":
    gateway = MqttGateway()
    new_device = Device(
        device_id="sensor:004",
        entity_name="urn:ngsi-ld:Sensor:004",
        entity_type="Sensor",
    )
    gateway.add_device(new_device)
    print(gateway.gateway_device.attributes)
    print(gateway.database.get_all_devices())
    gateway.remove_device(new_device)
    print(gateway.gateway_device.attributes)
    print(gateway.database.get_all_devices())
    gateway.database.delete_all_devices()
