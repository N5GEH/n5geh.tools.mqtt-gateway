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

received_messages = defaultdict(int)
sent_messages = defaultdict(int)

async def on_message(msg, num_clients):
    received_messages[num_clients] += 1

async def create_client(num_clients):
    async with MQTTClient(hostname=mqtt_broker_address, port=1883) as client:
        topic = f"test/latency/{num_clients}"
        while True:
            sent_messages[num_clients] += 1
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
                    print(f"Received info: {msg.payload.decode('utf-8')}")
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

def plot_message_loss(received_messages, sent_messages):
    num_clients_list = sorted(received_messages.keys())
    
    message_loss_data = []
    for num_clients in num_clients_list:
        message_loss = 1 - (received_messages[num_clients] / sent_messages[num_clients])
        message_loss_percentage = message_loss * 100
        message_loss_data.append({'num_clients': num_clients, 'message_loss_percentage': message_loss_percentage})
            
    message_loss_df = pd.DataFrame(message_loss_data)
    
    sns.set_theme(style="whitegrid")
    sns.barplot(data=message_loss_df, x='num_clients', y='message_loss_percentage', color='#e62332')
    plt.xlabel('Number of Concurrent Clients')
    plt.ylabel('Message Loss Percentage')
    plt.title('MQTT Broker Message Loss Percentage')
    plt.show()

plot_message_loss(received_messages, sent_messages)
