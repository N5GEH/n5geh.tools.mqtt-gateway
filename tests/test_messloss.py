import asyncio
import time
import json
from asyncio_mqtt import Client as MQTTClient
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

config = json.load(open("config.json"))
mqtt_broker_address = config["connection_settings"]["server_ip"]

sent_messages = Counter()
received_messages = defaultdict(Counter)

async def on_message(msg, num_clients):
    client_id, message_id = msg.payload.decode('utf-8').split(':')
    received_messages[num_clients][client_id] += 1
    print(f"Received message from client {client_id} with ID {message_id}")

async def create_client(client_id, num_clients):
    async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
        message_id = 0
        while True:
            message = f"{client_id}:{message_id}"
            await client.publish("test/message_loss", message)
            sent_messages[client_id] += 1
            message_id += 1
            await asyncio.sleep(1)

async def create_watcher(num_clients):
    async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
        async with client.filtered_messages("test/message_loss") as messages:
            await client.subscribe("test/message_loss")

            try:
                async for msg in messages:
                    await on_message(msg, num_clients)
            except asyncio.CancelledError:
                pass

max_clients = 1000
initial_clients = 100
client_step = 100
creation_interval = 12

async def main():
    watcher_tasks = []

    for num_clients in range(initial_clients, max_clients + 1, client_step):
        watcher_task = asyncio.create_task(create_watcher(num_clients))
        watcher_tasks.append(watcher_task)

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
    for task in client_tasks + watcher_tasks:
        task.cancel()

    # Wait for all tasks to complete or be cancelled
    await asyncio.gather(*client_tasks, *watcher_tasks, return_exceptions=True)

asyncio.run(main())

def plot_results(sent_messages, received_messages):
    num_clients_list = sorted(received_messages.keys())
    message_loss = []

    for num_clients in num_clients_list:
        total_sent = sum(sent_messages.values())
        total_received = sum(received_messages[num_clients].values())
        loss = (total_sent - total_received) / total_sent * 100
        message_loss.append(loss)

    plt.plot(num_clients_list, message_loss, marker='o')
    plt.xlabel('Number of Concurrent Clients')
    plt.ylabel('Message Loss (%)')
    plt.ylim(bottom=max(0, min(message_loss)), top=max(message_loss) + 1)
    plt.title('MQTT Broker Message Loss')
    plt.grid()
    plt.show()

plot_results(sent_messages, received_messages)
