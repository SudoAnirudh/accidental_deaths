import numpy as np
import matplotlib.pyplot as plt

# Data
causes = [
    "Avalanche", "Exposure to cold", "Cyclone", "Tornado", "Tsunami", "Earthquake", "Epidemic", "Flood",
    "Heat/Sun Stroke", "Landslide", "Lightning", "Torrential Rain", "Forest Fire", "Causes other than above",
    "Total"
]
genders = ["Male", "Female", "Transgender"]
data = np.array([
    [6, 2, 0, 8],
    [515, 103, 0, 618],
    [105, 13, 0, 118],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [448, 208, 0, 656],
    [312, 62, 0, 374],
    [247, 133, 0, 380],
    [2218, 661, 1, 2880],
    [44, 19, 0, 63],
    [13, 10, 0, 23],
    [1610, 393, 1, 2004],
    [5519, 1605, 2, 7126]
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("Total Number of Cases by Cause and Gender", fontsize=16)

# Plot the stacked bar chart
bar_width = 0.5
bar_positions = np.arange(len(causes))

bottom = np.zeros(len(causes))
for i, gender in enumerate(genders):
    ax.bar(
        bar_positions, data[:, i], bar_width, bottom=bottom, label=gender
    )
    bottom += data[:, i]

# Customize the plot
ax.set_xticks(bar_positions)
ax.set_xticklabels(causes, rotation=45, ha='right', fontsize=10)
ax.legend(loc="upper right", fontsize=10)
plt.tight_layout()

plt.show()
