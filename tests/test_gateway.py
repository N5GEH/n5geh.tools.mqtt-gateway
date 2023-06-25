import asyncio
import json
import time
from random import uniform
from typing import List

import asyncio_mqtt
import httpx
from asyncio_mqtt import Client as MQTTClient
from dateutil.parser import parse
from fastapi import FastAPI
from pydantic import BaseModel
from uvicorn import Config, Server
from aiologger import Logger
from aiologger.handlers.files import AsyncFileHandler
from filip.utils.cleanup import clear_context_broker, clear_iot_agent


from plots.plots import plot_latency, plot_message_loss, plot_percentage_loss
from utils.utils import generate_entity, generate_payload, register_device, register_entity, generate_subscription
import aiohttp
import sys
from collections import defaultdict
from uuid import uuid4
from filip.models.base import FiwareHeader
from jsonpath_ng import parse as parse_jsonpath


GATEWAY_URL = "http://localhost:8000"

FIWARE_HEADER = FiwareHeader(service="gateway", service_path="/gateway")

mqtt_broker_address = "localhost"
orion_address = "http://localhost:1026"

max_clients = 500
initial_clients = 50
client_step = 50
creation_interval = 30

stage_count = max_clients // client_step
messages_sent = [0] * stage_count
messages_received = [0] * stage_count
messages_per_second = [0] * stage_count
latencies = defaultdict(list)

stage = 0

last_message_received = asyncio.Event()
generate_messages = asyncio.Event()


async def register_datapoint(session: aiohttp.ClientSession, entity_id: str, entity_type: str, attribute_name: str) -> None:
    """
    Register a new datapoint for the given entity in the gateway using the API.
    """

    await session.post(f"{GATEWAY_URL}/data", json={
        "object_id": str(uuid4()),
        "jsonpath": f"$..{attribute_name}",
        "topic": f"test/{entity_id}",
        "description": "Test",
        "entity_id": entity_id,
        "entity_type": entity_type,
        "attribute_name": attribute_name,
        "matchDatapoint": True
    })

async def clear_gateway() -> None:
    """
    Clear all datapoints from the gateway.
    """
    async with aiohttp.ClientSession() as session:
        await session.delete(f"{GATEWAY_URL}/data")

async def receive_mqtt_notification() -> None:
    """
    Receive the notification from the Orion Context Broker via MQTT and calculate the latency.
    I will make use of the DateModified metadata field to calculate the latency. This field is automatically
    added by the Orion Context Broker and contains the timestamp of the last update of the entity. We can then
    calculate the latency by subtracting the timestamp attribute of the entity from the DateModified attribute.
    """
    async with asyncio_mqtt.Client("localhost") as client:
        await client.subscribe("test/timestamp")
        async with client.messages() as messages:
            async for message in messages:
                messages_received[stage] += 1
                last_message_received.set()
                payload = json.loads(message.payload)
                payload_timestamp = parse_jsonpath("$..value").find(payload)[0].value
                date_modified = parse(
                    parse_jsonpath("$..dateModified.value").find(payload)[0].value
                ).timestamp()
                latency = (date_modified - payload_timestamp) * 1000
                latencies[stage].append(latency)


async def generate_client() -> None:
    """
    Generate a client and publish a payload to the test/latency topic every second.
    The client continuously publishes a payload every second until it is cancelled. Each payload consists of
    a real and a fake attribute and a timestamp. The real attribute is used to test whether the matching works
    properly, while the timestamp is used to calculate the latency.
    """
    try:
        device_id, entity_id, entity_type, attribute_name = await generate_entity()
        async with aiohttp.ClientSession() as session:
            await register_datapoint(session, entity_id, entity_type, attribute_name)
            await register_entity(session, entity_id, entity_type, attribute_name)
            await generate_subscription(session, entity_id, entity_type, attribute_name)
        async with MQTTClient(mqtt_broker_address) as client:
            await client.connect()
            while True:
                await generate_messages.wait()
                await client.publish(f"test/{entity_id}", await generate_payload(attribute_name=attribute_name))
                messages_sent[stage] += 1
                await asyncio.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")


async def generate_clients(
        initial_clients: int, client_step: int, creation_interval: int
) -> None:
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
    logger = Logger.with_default_handlers(name="benchmark")
    logger.add_handler(AsyncFileHandler("benchmark.log", mode="a"))
    try:
        global stage
        for _ in range(max_clients // client_step):
            print(f"Stage {stage}")
            generate_messages.set()
            messages_per_second[stage] = client_step * (stage + 1)
            new_tasks = [
                asyncio.create_task(generate_client()) for _ in range(client_step)
            ]
            tasks.extend(new_tasks)
            await asyncio.sleep(creation_interval)
            generate_messages.clear()
            await wait_for_last_stage_message(10)
            stage += 1
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cancel all tasks
        for task in tasks:
            task.cancel()
        # Wait for all tasks to complete their cancellation
        await asyncio.gather(*tasks, return_exceptions=True)
        plot_message_loss(messages_sent, messages_received, messages_per_second)
        plot_percentage_loss(messages_sent, messages_received, messages_per_second)
        plot_latency(messages_per_second, latencies)
        await clear_gateway()
        clear_context_broker("http://localhost:1026", FIWARE_HEADER)

async def wait_for_last_stage_message(wait_time: int = 5):
    """
    Wait for the last message to be received during each stage. 
    If no message is received in the last wait_time seconds, it returns.
    """
    while True:
        try:
            await asyncio.wait_for(last_message_received.wait(), wait_time)
            last_message_received.clear()
        except asyncio.TimeoutError:
            print(f"No messages received in the last {wait_time} seconds. Moving to the next stage...")
            break


async def main():
    """
    Main function that starts the FastAPI server and generates the clients.
    The exception sent when the user presses CTRL+C is KeyboardInterrupt, which we need to handle gracefully here.
    Otherwise due to the async nature of the code, the code would continue running and the server would not be closed.
    """
    try:
        clear_context_broker("http://localhost:1026", FIWARE_HEADER)
        test_clients = asyncio.create_task(
            generate_clients(initial_clients, client_step, creation_interval)
        )
        sub_listen = asyncio.create_task(receive_mqtt_notification())
        await asyncio.gather(test_clients, sub_listen)
    except KeyboardInterrupt:
        print("Received exit signal. Shutting down...")
        for task in asyncio.all_tasks():
            task.cancel()
        await clear_gateway()
        print("Shutdown complete.")
        sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
