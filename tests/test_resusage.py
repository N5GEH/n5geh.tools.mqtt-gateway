import time
import psutil
import matplotlib.pyplot as plt

measurement_duration = 10  # in seconds
start_time = time.time()

cpu_percentages = []
memory_percentages = []
network_usage_sent = []
network_usage_received = []

while time.time() - start_time < measurement_duration:
    cpu_percentages.append(psutil.cpu_percent(interval=1))
    memory_percentages.append(psutil.virtual_memory().percent)
    network_counters = psutil.net_io_counters()
    network_usage_sent.append(network_counters.bytes_sent)
    network_usage_received.append(network_counters.bytes_recv)

# Plot resource usage graphs
plt.figure()
plt.plot(cpu_percentages)
plt.xlabel('Time (1 sec intervals)')
plt.ylabel('CPU Usage (%)')
plt.title('CPU Usage')

plt.figure()
plt.plot(memory_percentages)
plt.xlabel('Time (1 sec intervals)')
plt.ylabel('Memory Usage (%)')
plt.title('Memory Usage')

plt.figure()
plt.plot(network_usage_sent, label='Sent')
plt.plot(network_usage_received, label='Received')
plt.xlabel('Time (1 sec intervals)')
plt.ylabel('Network Usage (bytes)')
plt.title('Network Usage')
plt.legend()

plt.show()
