import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from typing import List
from collections import defaultdict


def plot_percentage_loss(messages_sent: List, messages_received: List, messages_per_second: List, baseline: bool = False) -> None:
    print(f"Messages sent: {messages_sent}")
    print(f"Messages received: {messages_received}")
    messages_sent = np.array(messages_sent)
    messages_received = np.array(messages_received)

    percentage_loss = (1 - messages_received / messages_sent) * 100

    x = np.arange(len(messages_per_second))  # the label locations

    fig, ax = plt.subplots(figsize=(10, 7))
    scatter = ax.scatter(x, percentage_loss, color="#ff7f0e", zorder=5)  # plot the dots on the graph
    ax.grid(True)  # add a grid

    # interpolate to get a smooth curve
    xnew = np.linspace(x.min(), x.max(), 500)
    spl = make_interp_spline(x, percentage_loss, k=3)
    ynew = spl(xnew)

    ax.plot(xnew, ynew, color="#ff7f0e")  # plot the curve

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel("Clients/s", fontsize=14)
    ax.set_ylabel("Percentage Loss", fontsize=14)
    ax.set_title("Percentage of Messages Lost", fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(messages_per_second, fontsize=14)
    ax.set_ylim(0, 100)  # ensure y-axis starts at 0% and ends at 100%

    # Annotate the exact percentage loss at each data point
    for (i, perc) in zip(x, percentage_loss):
        ax.annotate(f"{perc:.2f}%", (i, perc), textcoords="offset points", xytext=(0, 10), ha='center')

    fig.tight_layout()
    if baseline:
        plt.savefig("tests/results/baseline_message_loss_percentage.png")
    else:
        plt.savefig("tests/results/gateway_message_loss_percentage.png")
    plt.show()


def plot_message_loss(messages_sent: List, messages_received: List, messages_per_second: List, baseline: bool = False) -> None:
    print(f"Messages sent: {messages_sent}")
    print(f"Messages received: {messages_received}")
    messages_sent = np.array(messages_sent)
    messages_received = np.array(messages_received)

    percentage = messages_received / messages_sent * 100

    x = np.arange(len(messages_per_second))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 7))
    rects1 = ax.bar(x - width / 2, messages_sent, width, label="Messages Sent", color="#ff7f0e")
    rects2 = ax.bar(x + width / 2, messages_received, width, label="Messages Received")

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel("Clients/s", fontsize=14)
    ax.set_ylabel("Messages", fontsize=14)
    ax.set_title("Messages Sent vs Messages Received", fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(messages_per_second, fontsize=14)
    ax.legend(fontsize=14)

    for rect1, rect2, perc in zip(rects1, rects2, percentage):
        height1 = rect1.get_height()
        height2 = rect2.get_height()
        ax.annotate(
            f"{round(perc, 2)}%",
            xy=(rect2.get_x() + rect2.get_width() / 2, height2),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=14,
        )

    fig.tight_layout()
    if baseline:
        plt.savefig("tests/results/baseline_message_loss_bar.png")
    else:
        plt.savefig("tests/results/gateway_message_loss_bar.png")
    plt.show()

def plot_latency(messages_per_second: List, latencies: defaultdict, baseline: bool = False) -> None:
    """
    Plot the latency of the messages sent to the gateway.
    The plot is a boxplot with the latency on the y-axis and the number of clients on the x-axis.
    The box represents the interquartile range (IQR), the middle 50% of the data (25th percentile to the 75th percentile).
    The whiskers represent the range of the data, excluding the outliers. It is 1.5 times the IQR, leading to 90% of the data being within the whiskers.
    The median is the orange line.
    """
    x = np.arange(len(messages_per_second))  # the label locations

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.boxplot(latencies.values(), showfliers=False)
    ax.set_xticklabels(messages_per_second, fontsize=14)
    ax.set_xlabel("Clients/s", fontsize=14)
    ax.set_ylabel("Latency (ms)", fontsize=14)
    ax.set_title("Latency", fontsize=16)
    ax.grid(True)

    fig.tight_layout()
    if baseline:
        plt.savefig("tests/results/baseline_latency.png")
    else:
        plt.savefig("tests/results/gateway_latency.png")
    plt.show()