import numpy as np
import matplotlib.pyplot as plt

# Data
causes = [
    "Avalanche", "Exposure to cold", "Cyclone", "Tornado", "Tsunami", "Earthquake", "Epidemic", "Flood",
    "Heat/Sun Stroke", "Landslide", "Lightning", "Torrential Rain", "Forest Fire", "Causes other than above",
    "Total"
]
age_groups = ["60 years & Above - Male", "60 years & Above - Female", "60 years & Above - Transgender", "60 years & Above - Total"]
data = np.array([
    [1, 0, 0, 1],
    [131, 26, 0, 157],
    [4, 5, 0, 9],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [43, 23, 0, 66],
    [76, 17, 0, 93],
    [30, 22, 0, 52],
    [165, 34, 0, 199],
    [3, 0, 0, 3],
    [1, 2, 0, 3],
    [1115, 220, 0, 1335],
    [1569, 349, 0, 1918]
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Number of Cases by Cause and Age Group", fontsize=16)

# Plot the grouped bar chart
bar_width = 0.2
bar_positions = np.arange(len(causes))

for i, age_group in enumerate(age_groups):
    ax.bar(
        bar_positions + (i - 1) * bar_width, data[:, i], width=bar_width, label=age_group
    )

# Customize the plot
ax.set_xticks(bar_positions)
ax.set_xticklabels(causes, rotation=45, ha='right', fontsize=10)
ax.legend(loc="upper left", fontsize=10)
plt.tight_layout()

plt.show()
