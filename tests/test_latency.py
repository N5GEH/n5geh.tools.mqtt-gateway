# Why'd you have to go and make things so complicated?
# I see the way you're acting like you're somebody else
# Gets me frustrated
# Life's like this, you
# You async, you await, and you fetch
# And you say, "I'm a little bit of everything"
# But I'm a complicated app
# Oh no, no, no

import asyncio
import time
import json
from asyncio_mqtt import Client as MQTTClient
import matplotlib.pyplot as plt
from statistics import mean, stdev
from collections import defaultdict

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

latencies = defaultdict(list)

async def on_message(msg, num_clients):
    latency = time.time() - float(msg.payload.decode('utf-8'))
    latencies[num_clients].append(latency * 1000)
    print(f"Received info: {msg.payload.decode('utf-8')} with latency {latency * 1000} ms")

async def create_client():
    async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
        while True:
            await client.publish("test/latency", str(time.time()))
            await asyncio.sleep(1)

async def create_watcher(num_clients):
    async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
        async with client.filtered_messages("test/latency") as messages:
            await client.subscribe("test/latency")

            try:
                async for msg in messages:
                    await on_message(msg, num_clients)
            except asyncio.CancelledError:
                pass

max_clients = 100
initial_clients = 10
client_step = 10
creation_interval = 60

async def main():
    watcher_tasks = []

    for num_clients in range(initial_clients, max_clients + 1, client_step):
        watcher_task = asyncio.create_task(create_watcher(num_clients))
        watcher_tasks.append(watcher_task)

    client_tasks = []

    # Create initial clients
    for _ in range(initial_clients):
        client_tasks.append(asyncio.create_task(create_client()))

    # Add more clients in steps
    for i in range(initial_clients + client_step, max_clients + 1, client_step):
        await asyncio.sleep(creation_interval)
        for _ in range(client_step):
            client_tasks.append(asyncio.create_task(create_client()))

    # Wait for the last group of clients to run for the specified duration
    await asyncio.sleep(creation_interval)

    # Cancel all tasks
    for task in client_tasks + watcher_tasks:
        task.cancel()

    # Wait for all tasks to complete or be cancelled
    await asyncio.gather(*client_tasks, *watcher_tasks, return_exceptions=True)

asyncio.run(main())

def plot_results(latencies):
    means = []
    errors = []
    num_clients_list = sorted(latencies.keys())

    for num_clients in num_clients_list:
        latencies[num_clients] = latencies[num_clients][len(latencies[num_clients]) // 2:]
        mean_latency = mean(latencies[num_clients])
        std_dev = stdev(latencies[num_clients])
        error = 1.645 * (std_dev / (len(latencies[num_clients]) ** 0.5))

        means.append(mean_latency)
        errors.append(error)

    plt.errorbar(num_clients_list, means, yerr=errors, fmt='o', capsize=5)
    plt.xlabel('Number of Concurrent Clients')
    plt.ylabel('Latency (ms)')
    plt.title('MQTT Broker Latency (90% Confidence Interval)')
    plt.show()

plot_results(latencies)
