# testing out the multientity plugin

import paho.mqtt.client as mqtt
import json
import time
import requests
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient, QuantumLeapClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_context_broker, clear_iot_agent

from database import Database

config = json.load(open("config.json"))
orion = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"
iota_7896 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_http_port']}"
iota_4041 = f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}"
service = config["gateway_setup"]["fiware_service"]
servicepath = config["gateway_setup"]["fiware_servicepath"]


class MqttGateway:
    def __init__(self):
        s = requests.Session()
        self.iota_client = IoTAClient(url=iota_4041, session=s)

        self.database = Database()

        # create gateway device
        self.gateway_device = Device(
            device_id="gateway:001",
            entity_name="ngsi-ld:urn:Gateway:001",
            entity_type="Gateway",
            protocol="IoTA-UL",
            attributes=[
                DeviceAttribute(
                    object_id="sensor01",
                    name="sensor_living_room",
                    type="Number",
                    entity_name="urn:ngsi-ld:Sensor:001",
                    entity_type="Sensor",
                ),
                DeviceAttribute(
                    object_id="sensor02",
                    name="sensor_kitchen",
                    type="Number",
                    entity_name="urn:ngsi-ld:Sensor:002",
                    entity_type="Sensor",
                ),
                DeviceAttribute(
                    object_id="sensor03",
                    name="sensor_bathroom",
                    type="Number",
                    entity_name="urn:ngsi-ld:Sensor:003",
                    entity_type="Sensor",
                ),
            ],
        )

    def add_device(self, device: Device):
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

    def remove_device(self, device: Device):
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
