"""
Create dummy sensor signals to test the MQTT gateway
"""

from utils import load_topics
from paho.mqtt.client import Client, MQTTv5, MQTT_CLEAN_START_FIRST_ONLY
import threading
import uuid
import time
import json
from random import uniform

# Settings
HOST = "http://161.35.205.102"
PORT = 1883


class DummySensor:

    def __init__(self, topic: str = "example/topic", sampling_time: float = 1, n_attributes: int = 1):
        self.topic = topic
        self.mqtt_client = Client(protocol=MQTTv5)
        self.sampling_time = sampling_time

        def gen_attributes(n):
            return ["t" * (i + 1) for i in range(n)]
        self.attributes = gen_attributes(n_attributes)

    def gen_payload(self):
        # TODO maybe also test string values
        payload_dict = {attr: uniform(-10, 100) for attr in self.attributes}
        return json.dumps(payload_dict)

    def run(self):
        self.mqtt_client.connect(host=HOST,
                                 port=PORT,
                                 keepalive=60,
                                 bind_address="",
                                 bind_port=0,
                                 clean_start=MQTT_CLEAN_START_FIRST_ONLY,
                                 properties=None)

        self.mqtt_client.loop_start()
        while True:
            time.sleep(self.sampling_time)
            self.mqtt_client.publish(topic=self.topic, payload=self.gen_payload())


def start_new_sensor(*args):
    sensor = DummySensor(*args)
    sensor.run()


def add_new_sensor(*args):
    """Create a new client for the topic"""
    t = threading.Thread(target=start_new_sensor, daemon=True, args=args)
    t.start()


# get the registered topics
topics: list = load_topics()

# add three additional topics
topics.append(f"evil/{uuid.uuid4()}/{uuid.uuid4()}")
topics.append(f"evil/{uuid.uuid4()}/{uuid.uuid4()}")
topics.append(f"evil/{uuid.uuid4()}/{uuid.uuid4()}")

# TODO the goal is to write a script that generate dummy sensor measurements (at different )
sampling_lower = 0.5
sampling_upper = 10

for _topic in topics:
    sampling_t = uniform(sampling_lower, sampling_upper)
    # n_attr = int(uniform(0.5, 5.5))
    n_attr = 1
    add_new_sensor(_topic, sampling_t, n_attr)

while True:
    time.sleep(5)
    print("Dummy Sensor")
