import time
import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plt

sent_messages = 0
received_messages = 0

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

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

start_time = time.time()
measurement_duration = 10  # in seconds
sent_received = []

while time.time() - start_time < measurement_duration:
    time.sleep(0.1)
    client.publish("test/loss_rate", "test_message")
    sent_messages += 1
    sent_received.append((sent_messages, received_messages))

sent, received = zip(*sent_received)

# Plot message loss rate graph
plt.figure()
plt.plot(sent, label='Sent Messages')
plt.plot(received, label='Received Messages')
plt.xlabel('Time (0.1 sec intervals)')
plt.ylabel('Number of Messages')
plt.title('Message Loss Rate')
plt.legend()
plt.show()