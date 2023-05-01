# I intend to combine all the tests for the gateway into one file. 
# Work in progress.
from unittest import TestCase
from gateway.sensor import Lorawan
from random import randint
from gateway.gateway import Gateway

def generate_random_string(length: int) -> str:
    """Generate a random string of a given length

    Args:
        length (int): The length of the string

    Returns:
        str: The random string
    """
    import random
    import string

    return "".join(random.choice(string.ascii_letters) for i in range(length))

def generate_dummy_sensor(name: str, topic: str, attribute: str) -> Lorawan:
    """Generate a dummy sensor

    Returns:
        Lorawan: The dummy sensor
    """
    sensor = Lorawan(name, topic, attribute)
    sensor.payload = {
        f'{attribute}': generate_random_string(randint(1, 10))
    }
    return sensor


if __name__ == "__main__":
    for i in range(10):
        print(generate_random_string(randint(1, 10)))