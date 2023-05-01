# Oh async, my async
# You are the one that I adore
# And I'll never let you go
# Just like you never let await go before
# Oh async, my async
# You are my everything
import asyncio
import time
import json
from asyncio_mqtt import Client as MQTTClient
import matplotlib.pyplot as plt
from collections import defaultdict
from statistics import mean, stdev

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

connection_times = defaultdict(list)

async def create_client(client_id, num_clients):
    while True:
        start_time = time.time()
        async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
            connection_time = time.time() - start_time
            connection_times[num_clients].append(connection_time)
            print(f"Client {client_id} connected in {connection_time:.3f} seconds")
        await asyncio.sleep(1)

max_clients = 100
initial_clients = 10
client_step = 10
creation_interval = 60

async def main():
    client_tasks = []

    # Create initial clients
    for i in range(initial_clients):
        client_id = f"client_{i}"
        client_tasks.append(asyncio.create_task(create_client(client_id, initial_clients)))

    # Add more clients in steps
    for num_clients in range(initial_clients + client_step, max_clients + 1, client_step):
        await asyncio.sleep(creation_interval)
        for i in range(num_clients - client_step, num_clients):
            client_id = f"client_{i}"
            client_tasks.append(asyncio.create_task(create_client(client_id, num_clients)))

    # Wait for the last group of clients to run for the specified duration
    await asyncio.sleep(creation_interval)

    # Cancel all tasks
    for task in client_tasks:
        task.cancel()

    # Wait for all tasks to complete or be cancelled
    await asyncio.gather(*client_tasks, return_exceptions=True)

asyncio.run(main())

def plot_results(connection_times):
    num_clients_list = sorted(connection_times.keys())
    avg_connection_times = []
    errors = []

    for num_clients in num_clients_list:
        avg_time = mean(connection_times[num_clients])
        std_dev = stdev(connection_times[num_clients])
        error = 1.645 * (std_dev / (len(connection_times[num_clients]) ** 0.5))

        avg_connection_times.append(avg_time)
        errors.append(error)

    plt.errorbar(num_clients_list, avg_connection_times, yerr=errors, fmt='o', capsize=5)
    plt.xlabel('Number of Concurrent Clients')
    plt.ylabel('Average Connection Time (s)')
    plt.title('MQTT Broker Connection Rate (90% Confidence Interval)')
    plt.grid()
    plt.show()

plot_results(connection_times)
