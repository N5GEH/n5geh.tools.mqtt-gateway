from collections import defaultdict
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import os
import pickle
from datetime import datetime

TEST_ENV = os.environ.get("TEST_ENV", "gateway1x")
PRIMARY_COLOR = os.environ.get("PRIMARY_COLOR", "#6a5acd")
SECONDARY_COLOR = os.environ.get("SECONDARY_COLOR", "#ff7369")

def get_title(test_env: str) -> str:
    if test_env == "gateway1x":
        return "(1 gateway)"
    elif test_env == "gateway4x":
        return "(4 gateway cluster)"
    elif test_env == "baseline":
        return "(IoT Agent)"
    else:
        raise ValueError(f"Unknown test environment: {test_env} (must be one of 'gateway1x', 'gateway4x', 'baseline'))")

def plot_percentage_loss(
    messages_sent: List,
    messages_received: List,
    messages_per_second: List,
    baseline: bool = False,
) -> None:
    print(f"Messages sent: {messages_sent}")
    print(f"Messages received: {messages_received}")
    messages_sent = np.array(messages_sent)
    messages_received = np.array(messages_received)

    percentage_loss = (1 - messages_received / messages_sent) * 100

    x = np.arange(len(messages_per_second))  # the label locations

    fig, ax = plt.subplots(figsize=(10, 7))
    scatter = ax.scatter(
        x, percentage_loss, color=PRIMARY_COLOR, zorder=5
    )  # plot the dots on the graph
    ax.grid(True)  # add a grid

    # interpolate to get a smooth curve
    xnew = np.linspace(x.min(), x.max(), 500)
    spl = make_interp_spline(x, percentage_loss, k=3)
    ynew = spl(xnew)

    ax.plot(xnew, ynew, color=PRIMARY_COLOR, zorder=0)  # plot the curve

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel("Clients/s", fontsize=14)
    ax.set_ylabel("Percentage Loss", fontsize=14)
    ax.set_title(f"Percentage of Messages Lost {get_title(TEST_ENV)}", fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(messages_per_second, fontsize=14)
    ax.set_ylim(0, 100)  # ensure y-axis starts at 0% and ends at 100%

    # Annotate the exact percentage loss at each data point
    for i, perc in zip(x, percentage_loss):
        ax.annotate(
            f"{perc:.2f}%",
            (i, perc),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )
    
    ax.legend([scatter], ["Message Percentage Lost"], fontsize=14)

    fig.tight_layout()
    plt.savefig(f"tests/results/{TEST_ENV}_message_loss_percentage.png")
    with open(f"tests/results/pickles/{TEST_ENV}_message_loss_percentage.pickle", "wb") as f:
        pickle.dump((messages_sent, messages_received, messages_per_second), f, pickle.HIGHEST_PROTOCOL)
    plt.show()


def plot_message_loss(
    messages_sent: List,
    messages_received: List,
    messages_per_second: List,
    baseline: bool = False,
) -> None:
    print(f"Messages sent: {messages_sent}")
    print(f"Messages received: {messages_received}")
    messages_sent = np.array(messages_sent)
    messages_received = np.array(messages_received)

    percentage = messages_received / messages_sent * 100

    x = np.arange(len(messages_per_second))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 7))
    rects1 = ax.bar(
        x - width / 2, messages_sent, width, label="Messages Sent", color=PRIMARY_COLOR
    )
    rects2 = ax.bar(x + width / 2, messages_received, width, label="Messages Received", color=SECONDARY_COLOR)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel("Clients/s", fontsize=14)
    ax.set_ylabel("Messages", fontsize=14)
    ax.set_title(f"Messages Sent vs Messages Received {get_title(TEST_ENV)}", fontsize=16)
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
            bbox=dict(boxstyle='round,pad=0.33', alpha=0.33, color='grey'),
        )

    fig.tight_layout()
    plt.savefig(f"tests/results/{TEST_ENV}_message_loss_bar.png")
    with open(f"tests/results/pickles/{TEST_ENV}_message_loss_bar.pickle", "wb") as f:
        pickle.dump((messages_sent, messages_received, messages_per_second), f, pickle.HIGHEST_PROTOCOL)
    plt.show()


def plot_latency(
    messages_per_second: List, latencies: defaultdict, baseline: bool = False
) -> None:
    """
    Plot the latency of the messages sent to the gateway.
    The plot is a boxplot with the latency on the y-axis and the number of clients on the x-axis.
    The box represents the interquartile range (IQR), the middle 50% of the data (25th percentile to the 75th percentile).
    The whiskers represent the range of the data, excluding the outliers. It is 1.5 times the IQR, leading to 90% of the data being within the whiskers.
    The median is the orange line.
    """
    x = np.arange(len(messages_per_second))  # the label locations

    fig, ax = plt.subplots(figsize=(10, 7))
    median_props = dict(linestyle="-", linewidth=1, color=PRIMARY_COLOR)
    bp = ax.boxplot(latencies.values(), showfliers=False, medianprops=median_props)
    ax.set_xticklabels(messages_per_second, fontsize=14)
    ax.set_xlabel("Clients/s", fontsize=14)
    ax.set_ylabel("Latency (ms)", fontsize=14)
    ax.set_title(f"Latency {get_title(TEST_ENV)}", fontsize=16)
    ax.grid(True)

    fig.tight_layout()
    plt.savefig(f"tests/results/{TEST_ENV}_latency.png")
    with open(f'tests/results/pickles/{TEST_ENV}_latencies.pickle', 'wb') as f:
        pickle.dump((messages_per_second, latencies), f, protocol=pickle.HIGHEST_PROTOCOL)
    plt.show()

# in case one needs to plot the data again using the pickles
if __name__ == "__main__":
    TEST_ENV = "gateway1x"
    with open(f"tests/results/pickles/{TEST_ENV}_latencies.pickle", "rb") as f:
        messages_per_second, latencies = pickle.load(f)
    plot_latency(messages_per_second, latencies)
