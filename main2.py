import paho.mqtt.client as mqtt
import json
import time
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient, QuantumLeapClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from gateway.gateway import Gateway

SERVER_IP = '161.35.205.102'
ORION_PORT = 1026
MQTT_PORT = 1883
IOTA_PORT = 4041
QL_PORT = 8668
KAFKA_PORT = 9092

SERVICE = 'mqtt_gateway'
SERVICE_PATH = '/mqtt_gateway'

temperature_sensor = Device(device_id='device:001',
                            entity_name='urn:ngsi-ld:Device:001',
                            entity_type='TemperatureSensor',
                            protocol='IoTA-JSON',
                            transport='MQTT',
                            attributes=[DeviceAttribute(name='temperature',
                                                        object_id='t',
                                                        type='Number')])

def main():
    mqtt_gateway = Gateway()
    mqtt_gateway.connect(config['connection_settings']['server_ip'], config['connection_settings']['mqtt_port'], 60)
    mqtt_gateway.loop_start()
    for i in range(3):
        time.sleep(5)
        print(f"Publishing {i}")
        mqtt_gateway.publish("/gateway", json.dumps({"device_id": temperature_sensor.device_id}))
    print(mqtt_gateway.device_topics)
    mqtt_gateway.loop_stop()
    mqtt_gateway.disconnect()

if __name__ == '__main__':
    config = json.load(open('config.json'))
    main()
