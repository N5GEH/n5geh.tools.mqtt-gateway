import asyncio
import time
import json
from asyncio_mqtt import Client as MQTTClient
import matplotlib.pyplot as plt
from statistics import mean, stdev
from collections import defaultdict
from random import uniform
import requests
from fastapi import FastAPI, Request
from uvicorn import Config, Server
from pydantic import BaseModel
import httpx
from typing import List
from dateutil.parser import parse


config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]
orion_address = f"http://{config['connection_settings']['server_ip']}:1026"


max_clients = 100
initial_clients = 10
client_step = 10
creation_interval = 15

class Metadata(BaseModel):
    type: str
    value: str

class Attribute(BaseModel):
    type: str
    value: str
    metadata: dict[str, Metadata]

class Entity(BaseModel):
    id: str
    type: str
    temperature: Attribute
    humidity: Attribute
    pressure: Attribute
    co2: Attribute

class Notification(BaseModel):
    subscriptionId: str
    data: List[Entity]    

async def generate_subscription() -> int:
    """
    Generate a subscription for the test/latency topic. This is used to test the latency of the Orion Context Broker.
    The idea is to generate a subscription for the topic and then publish a message to the topic. The subscription should
    then be triggered and the message should be forwarded to the specified endpoint. We can then measure the latency
    between the publishing of the message and the reception of the message at the endpoint.
    """
    subscription = {
    "description": "Latency test subscription",
    "subject": {
        "entities": [
            {
                "id": "TestFacility",
                "type": "Room"
            }
        ],
        "condition": {
            "attrs": ["temperature", "humidity", "pressure", "co2"]
        }
    },
    "notification": {
        "http": {
            "url": "http://host.docker.internal:8001/latency/notification"
        },
        "attrs": ["temperature", "humidity", "pressure", "co2"],
        "metadata": ["dateCreated", "dateModified"]
    },
    "expires": "2040-01-01T14:00:00.00Z"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:1026/v2/subscriptions", json=subscription, headers={'Content-Type': 'application/json'})
        return response.status_code

async def start_server() -> None:
    """
    Start the FastAPI server that will receive the notifications from the Orion Context Broker.
    """
    app = FastAPI()
    @app.post("/latency/notification")
    async def receive_notification(notification: Notification) -> dict:
        """
        Receive a notification from the Orion Context Broker and calculate the latency.
        This function is called whenever a notification is received from the Orion Context Broker.
        The notification contains the payload that was published to the topic, as well as the metadata of the payload
        which contains the timestamp of the payload. We can then calculate the latency by subtracting the timestamp of the payload
        from the current timestamp. We iterate over all attributes of the payload and pick the one with the latest timestamp because
        this is the one that was published last and therefore the one that triggered the notification.

        Args:
            notification (Notification): The notification that was received from the Orion Context Broker.
            For structure, see the pydantic models above.

        Returns:
            dict: _description_
        """
        latest_attribute = max(
            (attr for attr in [notification.data[0].temperature, notification.data[0].humidity, notification.data[0].pressure, notification.data[0].co2]),
            key=lambda attr: parse(attr.metadata["dateModified"].value).timestamp(),
        )
        # Parse the timestamp from the payload
        payload_timestamp = parse(latest_attribute.metadata["dateModified"].value).timestamp()

        # Get the current time
        current_timestamp = time.time()
        
        # Calculate the latency
        latency = current_timestamp - payload_timestamp
        print(f"Latency: {latency:.3f} seconds")
        return {"latency": latency}
    config = Config(app=app, host="0.0.0.0", port=8001)
    server = Server(config=config)
    await server.serve()
    
async def generate_random_string(length: int) -> str:
    """
    Generate a random string of the specified length. This is used to generate random attribute names
    that are not already in use by the Orion Context Broker as we need to see whether the matching works properly.
    This is a very naive implementation, but it is sufficient for our purposes and makes use of the ascii table.
    At the end of the day, we just need to generate an 'attribute name' that is not registered in the Context Broker entity.
    """
    return "".join([chr(int(uniform(97, 122))) for _ in range(length)])

async def generate_payload() -> json:
    """
    Generate a random payload for the test/latency topic. The payload needs to contain a 'real' attribute (the one that exists in the Context Broker)
    and a 'fake' attribute (generated by generate_random_string) to test whether the matching works properly. The 'real' attribute will be picked at random
    from the list of attributes that are already in use by the Context Broker. Also, we need to add a timestamp to the payload so that we can calculate the latency.
    """
    attributes = ["temperature", "humidity", "pressure", "co2"]
    real_attribute = attributes[int(uniform(0, len(attributes)))]
    fake_attribute = await generate_random_string(10)
    return json.dumps({real_attribute: round(uniform(0, 100), 2), fake_attribute: round(uniform(0, 100), 2), "timestamp": time.time()})
    
async def generate_client() -> None:
    """
    Generate a client and publish a payload to the test/latency topic every second.
    The client continuously publishes a payload every second until it is cancelled. Each payload consists of 
    a real and a fake attribute and a timestamp. The real attribute is used to test whether the matching works 
    properly, while the timestamp is used to calculate the latency.
    """
    try:
        async with MQTTClient(mqtt_broker_address) as client:
            await client.connect()
            while True:
                await client.publish("test/latency", await generate_payload())
                await asyncio.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")

async def generate_clients(initial_clients: int, client_step: int, creation_interval: int) -> None:
    """
    Generate a number of clients and publish a payload to the test/latency topic every second (potentially one could extend this to publish to different topics as well).
    The number of clients is increased by client_step every creation_interval seconds. This is done to simulate a real-world scenario where the multiple clients
    try to publish data to the broker at the same time. The client_step and creation_interval parameters are used to control the number of clients and the interval
    between the creation of new clients respectively.

    Args:
        initial_clients (int): The number of clients to start with.
        client_step (int): The number of clients to add every creation_interval seconds.
        creation_interval (int): The interval between the creation of new clients.
    """
    tasks = []
    try:
        for _ in range(max_clients // client_step):
            new_tasks = [asyncio.create_task(generate_client()) for _ in range(client_step)]
            tasks.extend(new_tasks)
            await asyncio.sleep(creation_interval)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cancel all tasks
        for task in tasks:
            task.cancel()
        # Wait for all tasks to complete their cancellation
        await asyncio.gather(*tasks, return_exceptions=True)

async def main():
    """
    Main function that starts the FastAPI server and generates the clients.
    The exception sent when the user presses CTRL+C is KeyboardInterrupt, which we need to handle gracefully here.
    Otherwise due to the async nature of the code, the code would continue running and the server would not be closed.
    """
    try:
        server = asyncio.create_task(start_server())
        test_clients = asyncio.create_task(generate_clients(initial_clients, client_step, creation_interval))
        await asyncio.gather(server, test_clients)
    except KeyboardInterrupt:
        print("Received exit signal. Shutting down...")
        for task in asyncio.all_tasks():
            task.cancel()
        await server.aclose()  # Close the FastAPI server
        print("Shutdown complete.")

if __name__ == "__main__":
    asyncio.run(main())