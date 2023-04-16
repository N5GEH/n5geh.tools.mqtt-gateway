import time
import threading
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import json

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

def connect_device(device_id):
    client = mqtt.Client(client_id=f"device_{device_id}")
    client.connect(mqtt_broker_address, 1883, 60)
    client.loop_start()

num_devices = 100
connection_times = []

for i in range(num_devices):
    start_time = time.time()
    threading.Thread(target=connect_device, args=(i,)).start()
    connection_times.append(time.time() - start_time)

time.sleep(10)  # Allow time for connections to complete

# Plot connection rate graph
plt.figure()
plt.plot(connection_times)
plt.xlabel('Device Index')
plt.ylabel('Connection Time (s)')
plt.title('Connection Rate')
plt.show()
