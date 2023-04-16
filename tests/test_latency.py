import time
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import json

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

latencies = []

def on_connect(client, userdata, flags, rc):
    client.subscribe("test/latency")

def on_message(client, userdata, msg):
    latency = time.time() - float(msg.payload.decode('utf-8'))
    latencies.append(latency * 1000)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("mqtt_broker_address", 1883, 60)
client.loop_start()

measurement_duration = 60  # in seconds
start_time = time.time()

while time.time() - start_time < measurement_duration:
    time.sleep(1)
    client.publish("test/latency", time.time())

# Plot latency graph
plt.figure()
plt.plot(latencies)
plt.xlabel('Message Index')
plt.ylabel('Latency (ms)')
plt.title('Latency')
plt.show()
