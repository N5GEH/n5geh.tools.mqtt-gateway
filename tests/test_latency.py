import time
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import json
import numpy as np
import threading

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

latencies = []

def on_connect(client, userdata, flags, rc):
    client.subscribe("test/latency")

def on_message(client, userdata, msg):
    latency = time.time() - float(msg.payload.decode('utf-8'))
    latencies.append(latency * 1000)

def send_messages(freq):
    while True:
        time.sleep(1)
        client.publish("test/latency", time.time())
        msg_per_sec.append(freq)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address, 1883, 60)
client.loop_start()

num_threads = 100
threads_per_step = 10
step_duration = 5  # in seconds
msg_per_sec = []

for step in range(0, num_threads, threads_per_step):
    for _ in range(threads_per_step):
        t = threading.Thread(target=send_messages, args=(step + 1,)).start()
        print(f"Started thread {t} with frequency {step + 1}")
    time.sleep(step_duration)

client.loop_stop()

# Calculate mean latency and 90% confidence interval for each frequency step
latency_data = np.array(latencies).reshape(-1, step_duration)
mean_latencies = np.mean(latency_data, axis=1)
confidence_interval = 1.645 * np.std(latency_data, axis=1) / np.sqrt(step_duration)
# the 1.645 factor is the z-score for a 90% confidence interval
# https://www.statisticshowto.com/probability-and-statistics/confidence-interval/
# is presuming a normal distribution of the data sensible here?

# Plot latency graph with error bars
plt.figure()
plt.errorbar(np.arange(1, num_threads + 1, threads_per_step), mean_latencies, yerr=confidence_interval, fmt='o-', capsize=5, label="Mean Latency with 90% Confidence Interval")
plt.xlabel('Messages per Second')
plt.ylabel('Latency (ms)')
plt.title('Latency vs Messages per Second')
plt.legend()
plt.grid(True)
plt.show()
