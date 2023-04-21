# future entry point for the gateway
# work in progress for now

import paho.mqtt.client as mqtt
import json
import time
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_context_broker, clear_iot_agent

from gateway.gateway import MqttGateway


temperature_sensor = Device(device_id='device:001',
                            entity_name='urn:ngsi-ld:Device:001',
                            entity_type='TemperatureSensor',
                            protocol='IoTA-JSON',
                            transport='MQTT',
                            attributes=[DeviceAttribute(name='temperature',
                                                        object_id='t',
                                                        type='Number')])

def initial_setup() -> IoTAClient | ContextBrokerClient:
    fiware_header = FiwareHeader(service=config['gateway_setup']['fiware_service'],
                                 service_path=config['gateway_setup']['fiware_servicepath'])
    clear_iot_agent(f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}", fiware_header=fiware_header)
    clear_context_broker((f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}"), fiware_header=fiware_header)
    iotac = IoTAClient(f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['iota_port']}", fiware_header=fiware_header)
    cbc = ContextBrokerClient(f"http://{config['connection_settings']['server_ip']}:{config['connection_settings']['orion_port']}", fiware_header=fiware_header)
    return iotac, cbc


def main():
    iotac, cbc = initial_setup()
    iotac.post_device(device=temperature_sensor, update=True)
    mqtt_gateway = MqttGateway()
    for i in range(3):
        time.sleep(1)
        print(f"Publishing {i}")
        mqtt_gateway.publish("/gateway", json.dumps({"device_id": temperature_sensor.device_id, "temperature": i, "timestamp": time.time()}))
        time.sleep(3)
    print(mqtt_gateway.device_topics)
    mqtt_gateway.remove_device_topic(temperature_sensor.device_id)
    print(mqtt_gateway.device_topics)

if __name__ == '__main__':
    config = json.load(open('config.json'))
    main()
