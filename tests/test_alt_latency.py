import asyncio
import time
import json
from asyncio_mqtt import Client as MQTTClient
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

latencies = defaultdict(list)

async def on_message(msg, num_clients):
    latency = time.time() - float(msg.payload.decode('utf-8'))
    latencies[num_clients].append(latency * 1000)
    print(f"Received info: {msg.payload.decode('utf-8')} with latency {latency * 1000:.3f} ms")

async def create_client(num_clients):
    async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
        topic = f"test/latency/{num_clients}"
        while True:
            await client.publish(topic, str(time.time()))
            await asyncio.sleep(1)

async def create_watcher(num_clients):
    async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
        topic = f"test/latency/{num_clients}"
        async with client.filtered_messages(topic) as messages:
            await client.subscribe(topic)

            try:
                async for msg in messages:
                    await on_message(msg, num_clients)
            except asyncio.CancelledError:
                pass

max_clients = 1200
initial_clients = 100
client_step = 100
creation_interval = 60

async def main():
    client_tasks = []
    watcher_tasks = []

    for num_clients in range(initial_clients, max_clients + 1, client_step):
        # Create new clients
        for _ in range(num_clients):
            client_tasks.append(asyncio.create_task(create_client(num_clients)))

        # Create a new watcher for the current number of clients
        watcher_task = asyncio.create_task(create_watcher(num_clients))
        watcher_tasks.append(watcher_task)
        await asyncio.sleep(creation_interval)

    # Wait for the last group of clients to run for the specified duration
    await asyncio.sleep(creation_interval)

    # Cancel all tasks
    for task in client_tasks + watcher_tasks:
        task.cancel()

    # Wait for all tasks to complete or be cancelled
    await asyncio.gather(*client_tasks, *watcher_tasks, return_exceptions=True)
    
asyncio.run(main())

def plot_results_seaborn(latencies):
    num_clients_list = sorted(latencies.keys())
    
    latency_data = []
    for num_clients in num_clients_list:
        for latency in latencies[num_clients]:
            latency_data.append({'num_clients': num_clients, 'latency': latency})
            
    latency_df = pd.DataFrame(latency_data)
    
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(8, 6))
    sns.pointplot(data=latency_df, x='num_clients', y='latency', errorbar=('ci', 90), capsize=.2, markers='o', linestyles='')
    plt.xlabel('Number of Concurrent Clients')
    plt.ylabel('Latency (ms)')
    plt.title('MQTT Broker Latency (90% Confidence Interval)')
    plt.show()

plot_results_seaborn(latencies)
