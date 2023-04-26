import time
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import json
from collections import defaultdict

def moving_average(data, window_size):
    if len(data) < window_size:
        return data
    return [sum(data[i:i+window_size])/window_size for i in range(len(data) - window_size + 1)]

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

bandwidths = defaultdict(list)

def on_connect(client, userdata, flags, rc):
    client.subscribe("test/bandwidth")

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    size, timestamp = payload['size'], payload['timestamp']
    elapsed_time = time.perf_counter() - float(timestamp)
    message_size = len(msg.payload)
    bandwidth = (message_size * 8) / (elapsed_time * 1000)
    bandwidths[int(size)].append(bandwidth)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address, 1883, 60)
client.loop_start()

measurement_duration = 15  # in seconds
message_sizes = [1024, 2048, 4096, 8192, 16384, 32768, 65536]
start_time = time.perf_counter()

while time.perf_counter() - start_time < measurement_duration:
    time.sleep(0.1)
    
    for size in message_sizes:
        payload = {'size': size, 'timestamp': time.perf_counter(), 'data': 'a' * size}
        client.publish("test/bandwidth", json.dumps(payload))

# Plot bandwidth graph
plt.figure()
window_size = 5
for size in message_sizes:
    plt.plot(moving_average(bandwidths[size], window_size)[:-(window_size-1)], label=f"{size} Bytes")
plt.xlabel('Message Index')
plt.ylabel('Bandwidth (Kbps)')
plt.yscale('log')
plt.title(f'Bandwidth (Window size {window_size})')
plt.legend()
plt.show()
