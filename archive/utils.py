import pandas as pd
import threading
from converter import TopicConverter


def add_new_client(*args):
    mqtt_converter = TopicConverter(*args)
    mqtt_converter.run()


def add_topic(topic: str, *args):
    """Create a new client for the topic"""
    t = threading.Thread(target=add_new_client, daemon=True, name=topic, args=(topic, *args))  # TODO use name to identify the object?
    t.start()


def load_topics():
    path_topics = "data/topics.csv"
    df = pd.read_csv(path_topics, index_col=0)
    return list(df.values[:, 0])
