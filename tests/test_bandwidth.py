import time
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import json

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

bandwidths = []

def on_connect(client, userdata, flags, rc):
    client.subscribe("test/bandwidth")

def on_message(client, userdata, msg):
    elapsed_time = time.time() - float(msg.payload.decode('utf-8').split(',')[1])
    message_size = len(msg.payload)
    bandwidth = (message_size * 8) / (elapsed_time * 1000)
    bandwidths.append(bandwidth)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address, 1883, 60)
client.loop_start()

measurement_duration = 15  # in seconds
message_sizes = [1, 10, 100, 1000, 10000]  # Change or add more sizes as needed
start_time = time.time()

while time.time() - start_time < measurement_duration:
    time.sleep(1)
    
    for size in message_sizes:
        payload = f"{size * 'a'},{time.time()}"
        client.publish("test/bandwidth", payload)

# Plot bandwidth graph
plt.figure()
plt.plot(bandwidths)
plt.xlabel('Message Index')
plt.ylabel('Bandwidth (Kbps)')
plt.title('Bandwidth')
plt.show()
