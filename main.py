import paho.mqtt.client as mqtt
import json
import time

SERVER_IP = '161.35.205.102'
ORION_PORT = 1026
MQTT_PORT = 1883
IOTA_PORT = 4041
KAFKA_PORT = 9092

dummy_data = {
    "id": "urn:ngsi-ld:Sensor:001",
    "type": "Sensor",
    "category": {
        "type": "Property",
        "value": "temperature"
    }
}
    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/iot/d")
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+json.loads(msg.payload.decode('utf-8'))['id'])

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.connect(SERVER_IP, MQTT_PORT)
    
    mqtt_client.loop_start()
    for i in range(3):
        mqtt_client.publish("/iot/d", json.dumps(dummy_data))
        time.sleep(1)
        
    mqtt_client.loop_stop()
    pass
    
if __name__ == '__main__':
    main()