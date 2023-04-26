import time
import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plt

num_messages = 0

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]


def on_connect(client, userdata, flags, rc):
    client.subscribe("test/throughput")

def on_message(client, userdata, msg):
    global num_messages
    num_messages += 1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker_address, 1883, 60)
client.loop_start()

start_time = time.time()
measurement_duration = 10
message_count = []

while time.time() - start_time < measurement_duration:
    time.sleep(0.1)
    client.publish("test/throughput", "test_message")
    message_count.append(num_messages)

# Plot message throughput graph
plt.figure()
plt.plot(message_count)
plt.xlabel('Time (0.1 sec intervals)')
plt.ylabel('Number of Messages')
plt.title('Message Throughput')
plt.show()