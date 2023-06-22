import asyncio
from asyncio_mqtt import Client as MQTTClient


async def generate_client(event: asyncio.Event, mqtt_hostname: str = "localhost", mqtt_port: int = 1883):
    """
    Generate a client and publish a payload to the test/latency topic every second.
    The client continuously publishes a payload every second until it is cancelled. Each payload consists of
    a real and a fake attribute and a timestamp. The real attribute is used to test whether the matching works
    properly, while the timestamp is used to calculate the latency.
    """
    try:
        async with MQTTClient(mqtt_hostname) as client:
            await event.wait()
            await client.connect()
            while True:
                await client.publish("test/latency", await generate_payload())
                await asyncio.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")



