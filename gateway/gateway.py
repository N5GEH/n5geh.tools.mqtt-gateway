import paho.mqtt.client as mqtt
import json
import time
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient, QuantumLeapClient
from filip.clients.mqtt import IoTAMQTTClient
from filip.models.base import FiwareHeader
from filip.models.ngsi_v2.iot import Device, DeviceAttribute, ServiceGroup
from filip.utils.cleanup import clear_context_broker, clear_iot_agent


class Gateway(IoTAMQTTClient):
    def __init__(self):
        config = json.load(open('config.json'))
        super().__init__(client_id="mqtt_gateway",
                         protocol=mqtt.MQTTv311,
                         clean_session=True)
        self.device_topics = {}
        self.connect(config['connection_settings']['server_ip'], config['connection_settings']['mqtt_port'], 60)
        self.loop_start()

    def on_connect(self, client, userdata, flags, rc) -> None:
        print(f"Connected with result code {rc}")
        client.subscribe("/gateway")

    def on_message(self, client, userdata, message) -> None:
        msg = json.loads(message.payload.decode('utf-8'))
        device_id = msg['device_id']
        latency = (time.time() - msg['timestamp']) * 1000 # in ms
        if device_id not in self.device_topics:
            self.device_topics[device_id] = self.get_device_topic(device_id)
            client.subscribe(self.device_topics[device_id])
            print(f"Subscribed to {self.device_topics[device_id]}")
        print(f"Received message: {message.payload.decode('utf-8')} with latency {latency:.2f} ms")

    def get_device_topic(self, device_id) -> str:
        if device_id not in self.device_topics:
            self.device_topics[device_id] = f"/devices/{device_id}/data"
            return f"/devices/{device_id}/data"
        else:
            return self.device_topics[device_id]

    def remove_device_topic(self, device_id) -> None:
        if device_id in self.device_topics:
            del self.device_topics[device_id]
        else:
            print(f"Device {device_id} not in device_topics")
            
    def run(self) -> None:
        self.loop_forever()
    
    def __del__(self) -> None:
        self.loop_stop()
        self.disconnect()
