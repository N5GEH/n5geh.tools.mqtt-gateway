import time
import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import json

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

received_messages = 0
msg_per_sec = []
message_loss_rates = []

def on_connect(client, userdata, flags, rc):
    client.subscribe("test/loss_rate")

def on_message(client, userdata, msg):
    global received_messages
    received_messages += 1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address, 1883, 60)
client.loop_start()

num_messages = 10
num_iterations = 10

for freq in range(0, num_iterations * 10, 10):
    sent_messages = 0
    received_messages = 0
    current_msg_rate = freq + 1
    msg_per_sec.append(current_msg_rate)
    
    for _ in range(num_messages):
        sleep_interval = 1 / current_msg_rate
        time.sleep(sleep_interval)
        client.publish("test/loss_rate", "test_message")
        sent_messages += 1

    # Give some time for the last messages to be received before calculating the loss rate
    time.sleep(2)
    message_loss_rate = (sent_messages - received_messages) / sent_messages
    message_loss_rates.append(message_loss_rate)

client.loop_stop()

# Smooth curve using spline interpolation
x = np.array(msg_per_sec)
y = np.array(message_loss_rates)
x_smooth = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

plt.figure()
plt.scatter(x, y, marker='o', label="Message Loss Rate")
plt.plot(x_smooth, y_smooth, label="Smoothed Message Loss Rate")
plt.xlabel('Messages per Second')
plt.ylabel('Message Loss Rate')
plt.ylim(0, 0.1)
plt.title('Message Loss Rate vs Messages per Second')
plt.legend()
plt.grid(True)
plt.show()