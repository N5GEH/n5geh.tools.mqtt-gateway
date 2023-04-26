import time
import threading
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import numpy as np
import json

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

def connect_device(device_id):
    client = mqtt.Client(client_id=f"device_{device_id}")
    client.connect(mqtt_broker_address, 1883, 60)
    client.loop_start()

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size), 'valid') / window_size

num_devices = 100
connection_times = []
successful_connections = 0
window_size = 5

for i in range(num_devices):
    start_time = time.perf_counter()
    try:
        threading.Thread(target=connect_device, args=(i,)).start()
        connection_times.append(time.perf_counter() - start_time)
        successful_connections += 1
    except Exception as e:
        print(f"Error connecting device {i}: {e}")

time.sleep(10)  # Allow time for connections to complete

# Calculate connection success rate
success_rate = (successful_connections / num_devices) * 100

# Compute moving average
moving_avg = moving_average(connection_times, window_size)

plt.figure()
plt.plot(connection_times, '-.', label="Connection Times", alpha=0.5)
plt.plot(range(window_size - 1, num_devices), moving_avg, label=f"Moving Average (Window size {window_size})", linewidth=2)
plt.xlabel('Device Index')
plt.ylabel('Connection Time (s)')
plt.title(f'Connection Rate (Success Rate: {success_rate:.2f}%)')
plt.legend()
plt.show()
