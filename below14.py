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
    [0, 1, 0, 1],
    [16, 8, 0, 24],
    [3, 3, 0, 6],
    [0, 0, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [93, 67, 0, 160],
    [10, 1, 0, 11],
    [21, 13, 0, 34],
    [162, 67, 0, 229],
    [2, 5, 0, 7],
    [1, 0, 0, 1],
    [25, 15, 0, 40],
    [334, 180, 0, 514]
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Number of Cases by Cause and Gender", fontsize=16)

# Plot the grouped bar chart
bar_width = 0.2
bar_positions = np.arange(len(causes))

for i, gender in enumerate(genders):
    ax.bar(
        bar_positions + (i - 1) * bar_width, data[:, i], width=bar_width, label=gender
    )

# Customize the plot
ax.set_xticks(bar_positions)
ax.set_xticklabels(causes, rotation=45, ha='right', fontsize=10)
ax.legend(loc="upper right", fontsize=10)
plt.tight_layout()

plt.show()
