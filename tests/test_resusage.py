import time
import psutil
import threading
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import json
import numpy as np
from scipy.interpolate import make_interp_spline

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

def connect_device(device_id):
    client = mqtt.Client(client_id=f"device_{device_id}")
    client.connect(mqtt_broker_address, 1883, 60)
    client.loop_start()

num_devices = 100
resource_usage = []

for i in range(num_devices):
    start_time = time.time()
    threading.Thread(target=connect_device, args=(i,)).start()
    cpu_percent = psutil.cpu_percent(interval=0.1)
    memory_percent = psutil.virtual_memory().percent
    resource_usage.append((time.time() - start_time, cpu_percent, memory_percent))

time.sleep(10)  # Allow time for connections to complete

# Prepare data for the plot
x = [i for i in range(num_devices)]
y_cpu = [usage[1] for usage in resource_usage]
y_mem = [usage[2] for usage in resource_usage]

# Smooth curve using spline interpolation
x_smooth = np.linspace(min(x), max(x), 300)
spl_cpu = make_interp_spline(x, y_cpu, k=3)
y_cpu_smooth = spl_cpu(x_smooth)
spl_mem = make_interp_spline(x, y_mem, k=3)
y_mem_smooth = spl_mem(x_smooth)

# Plot the CPU usage graph
plt.figure()
plt.plot(x, y_cpu, label='Original CPU Usage', color='red', linewidth=1, alpha=0.5)
plt.plot(x_smooth, y_cpu_smooth, label='Smoothed CPU Usage', color='royalblue', linewidth=2)
plt.xlabel('Device Index')
plt.ylabel('CPU Usage (%)')
plt.title('Resource Usage: CPU')
plt.legend()
plt.grid(True)
plt.show()

# Plot the memory usage graph
plt.figure()
plt.plot(x, y_mem, label='Original Memory Usage', color='red', linewidth=1, alpha=0.5)
plt.plot(x_smooth, y_mem_smooth, label='Smoothed Memory Usage', color='darkorange', linewidth=2)
plt.xlabel('Device Index')
plt.ylabel('Memory Usage (%)')
plt.title('Resource Usage: Memory')
plt.legend()
plt.grid(True)
plt.show()
