import paho.mqtt.client as mqtt
import json
import time
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient, QuantumLeapClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_context_broker, clear_iot_agent

SERVER_IP = '161.35.205.102'
ORION_PORT = 1026
MQTT_PORT = 1883
IOTA_PORT = 4041
QL_PORT = 8668
KAFKA_PORT = 9092

SERVICE = 'mqtt_gateway'
SERVICE_PATH = '/mqtt_gateway'
API_KEY = SERVICE_PATH.strip('/')
    
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode('utf-8')}")

def main():    
    fiware_header = FiwareHeader(service=SERVICE, service_path=SERVICE_PATH)
    clear_context_broker(url=f"http://{SERVER_IP}:{ORION_PORT}", fiware_header=fiware_header)
    clear_iot_agent(url=f"http://{SERVER_IP}:{IOTA_PORT}", fiware_header=fiware_header)
    
    service_group = ServiceGroup(apikey=API_KEY, resource='/iot/json')
    
    temperature_sensor = Device(device_id='device:001',
                                entity_name='urn:ngsi-ld:Device:001',
                                entity_type='TemperatureSensor',
                                protocol='IoTA-JSON',
                                transport='MQTT',
                                apikey=API_KEY,
                                attributes=[DeviceAttribute(name='temperature',
                                                            object_id='t',
                                                            type='Number')])
    
    iotac = IoTAClient(url=f"http://{SERVER_IP}:{IOTA_PORT}", fiware_header=fiware_header)
    iotac.post_group(service_group=service_group, update=True)
    iotac.post_device(device=temperature_sensor, update=True)
    
    cbc = ContextBrokerClient(url=f"http://{SERVER_IP}:{ORION_PORT}", fiware_header=fiware_header)
    print(cbc.get_entity(temperature_sensor.entity_name).json(indent=2))
    
    mqttc = IoTAMQTTClient(protocol=mqtt.MQTTv5)
    mqttc.on_message = on_message
    mqttc.add_service_group(service_group)
    mqttc.add_device(temperature_sensor)
    mqttc.connect(SERVER_IP, MQTT_PORT)
    
    mqttc.loop_start()
    for i in range(3):
        print(f"Publishing {i}")
        mqttc.publish(device_id=temperature_sensor.device_id, payload={'t': i})
        time.sleep(1)
        
    mqttc.loop_stop()
    mqttc.disconnect()
    pass
    
if __name__ == '__main__':
    main()