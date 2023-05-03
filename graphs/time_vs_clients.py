import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
time = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600]
clients = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1000]

# Create a DataFrame
data = pd.DataFrame({'Time (s)': time, 'Clients': clients})

# Plot
sns.lineplot(x='Time (s)', y='Clients', data=data, drawstyle='steps-post', color='#E62332', linewidth=2.5)
plt.title('Clients vs Time')
plt.xlim(left=0, right=600)
plt.ylim(bottom=100, top=1000)

# Set x and y grid intervals
plt.xticks(np.arange(0, 601, 60))
plt.yticks(np.arange(100, 1001, 100))

plt.grid(True)

# Show the plot
plt.show()
