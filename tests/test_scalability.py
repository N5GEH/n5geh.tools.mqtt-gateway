import time
import threading
import paho.mqtt.client as mqtt
from concurrent.futures import ThreadPoolExecutor
import json

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

def connect_and_publish(device_id):
    client = mqtt.Client(client_id=f"device_{device_id}")
    client.connect(mqtt_broker_address, 1883, 60)
    client.loop_start()

    # Publish messages for a specified duration
    start_time = time.time()
    while time.time() - start_time < measurement_duration:
        time.sleep(0.1)
        client.publish(f"test/scalability/device_{device_id}", "test_message")

    client.loop_stop()

num_devices = 100
measurement_duration = 10  # in seconds

with ThreadPoolExecutor(max_workers=num_devices) as executor:
    futures = [executor.submit(connect_and_publish, i) for i in range(num_devices)]

# Wait for all threads to complete
for future in futures:
    future.result()

print(f"Scalability test completed with {num_devices} devices")
