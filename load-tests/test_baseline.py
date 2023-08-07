import asyncio
import json
import sys
from collections import defaultdict

import aiohttp
import asyncio_mqtt
from aiologger import Logger
from aiologger.handlers.files import AsyncFileHandler
from asyncio_mqtt import Client as MQTTClient
from dateutil.parser import parse
from filip.clients.ngsi_v2 import ContextBrokerClient, IoTAClient
from filip.models.base import FiwareHeader
from filip.utils.cleanup import clear_context_broker, clear_iot_agent
from jsonpath_ng import parse as parse_jsonpath
from plots.plots import plot_latency, plot_message_loss, plot_percentage_loss
from utils.utils import generate_entity, generate_payload, register_device, register_entity, generate_subscription
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
import random

MQTT_HOSTNAME = "137.226.248.161"
FIWARE_HEADER = FiwareHeader(service="baseline", service_path="/baseline")

MAX_CLIENTS = 450
INITIAL_CLIENTS = 50
CLIENT_STEP = 50
CREATION_INTERVAL = 30

STAGE_COUNT = MAX_CLIENTS // CLIENT_STEP

messages_sent = [0] * STAGE_COUNT
messages_received = [0] * STAGE_COUNT
messages_per_second = [0] * STAGE_COUNT
latencies = defaultdict(list)

stage = 0
clients_generated = 0
lock = asyncio.Lock()

last_message_received = asyncio.Event()
generate_messages = asyncio.Event()

jsonpath_expr = parse_jsonpath("$..value")
jsonpath_expr_modified = parse_jsonpath("$..dateModified.value")

process_executor = ProcessPoolExecutor(max_workers=cpu_count())


def process_message(message):
    last_message_received.set()
    payload = json.loads(message.payload)
    payload_timestamp = jsonpath_expr.find(payload)[0].value
    date_modified = parse(
        jsonpath_expr_modified.find(payload)[0].value
    ).timestamp()
    latency = (date_modified - payload_timestamp) * 1000
    return latency


async def receive_mqtt_notification(listener_id: int) -> None:
    async with MQTTClient(MQTT_HOSTNAME, keepalive=60000) as client:
        await client.subscribe(f"test/timestamp/{listener_id}")
        async with client.messages() as messages:
            async for message in messages:
                latency = await asyncio.get_running_loop().run_in_executor(process_executor, process_message, message)
                async with lock:
                    messages_received[stage] += 1
                latencies[stage].append(latency)
                print(f"Received message {messages_received[stage]}")


async def generate_client() -> None:
    """
    Generate a client and publish a payload to the test/latency topic every second.
    The client continuously publishes a payload every second until it is cancelled. Each payload consists of
    a real and a fake attribute and a timestamp. The real attribute is used to test whether the matching works
    properly, while the timestamp is used to calculate the latency.
    """
    device_id, entity_id, entity_type, attribute_name = await generate_entity()
    local_counter = [0] * STAGE_COUNT
    try:
        async with aiohttp.ClientSession() as session:
            # register a new entity with the Context Broker
            await register_entity(
                session,
                entity_id,
                entity_type,
                attribute_name,
            )
            # register a new device with the IoT Agent
            await register_device(
                session,
                device_id,
                entity_id,
                entity_type,
                attribute_name,
            )
            # generate a corresponding subscription
            await generate_subscription(
                session,
                entity_id,
                entity_type,
                attribute_name,
            )
    except Exception as e:
        pass
    # start the client
    try:
        async with MQTTClient(MQTT_HOSTNAME, client_id=device_id, keepalive=60000) as client:
            await client.connect()
            while True:
                await generate_messages.wait()
                await client.publish(
                    f"/1234/{device_id}/attrs",
                    await generate_payload(attribute_name),
                )
                local_counter[stage] += 1
                # If the event is not set, it means it is blocking
                await asyncio.sleep(1)
    except Exception as e:
        print(f"An error occurred while publishing the payload: {e}")
    finally:
        # Update messages_sent when the function ends
        for i in range(len(messages_sent)):
            messages_sent[i] += local_counter[i]


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
    try:
        global stage
        for _ in range(MAX_CLIENTS // client_step):
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
        # Cancel all tasks
        for task in tasks:
            task.cancel()
        # Wait for all tasks to complete their cancellation
        await asyncio.gather(*tasks, return_exceptions=True)
        # save the results to a pickle file
        # TODO
        # save_results_after_stage(messages_sent, messages_received, latencies, stage)
    finally:
        # Cancel all tasks
        for task in tasks:
            task.cancel()
        # Wait for all tasks to complete their cancellation
        await asyncio.gather(*tasks, return_exceptions=True)
        clear_context_broker(f"http://{MQTT_HOSTNAME}:1026", FIWARE_HEADER)
        clear_iot_agent(f"http://{MQTT_HOSTNAME}:4041", FIWARE_HEADER)
        plot_message_loss(
            messages_sent, messages_received, messages_per_second, baseline=True
        )
        plot_percentage_loss(
            messages_sent, messages_received, messages_per_second, baseline=True
        )
        plot_latency(messages_per_second, latencies, baseline=True)


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
            print(
                f"No messages received in the last {wait_time} seconds. Moving to the next stage..."
            )
            break


async def main():
    try:
        clear_context_broker(f"http://{MQTT_HOSTNAME}:1026", FIWARE_HEADER)
        clear_iot_agent(f"http://{MQTT_HOSTNAME}:4041", FIWARE_HEADER)
        test_clients = asyncio.create_task(
            generate_clients(INITIAL_CLIENTS, CLIENT_STEP, CREATION_INTERVAL)
        )
        # generate listeners to receive the notifications
        listeners = [
            asyncio.create_task(receive_mqtt_notification(i)) for i in range(4)
        ]
        await asyncio.gather(test_clients, *listeners)

    except KeyboardInterrupt:
        print("Received exit signal. Shutting down...")
        for task in asyncio.all_tasks():
            task.cancel()
        clear_context_broker(f"http://{MQTT_HOSTNAME}:1026", FIWARE_HEADER)
        clear_iot_agent(f"http://{MQTT_HOSTNAME}:4041", FIWARE_HEADER)
        print("Shutdown complete.")
        sys.exit(0)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())