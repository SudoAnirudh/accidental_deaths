import numpy as np
import matplotlib.pyplot as plt

# Data
causes = [
    "Avalanche", "Exposure to cold", "Cyclone", "Tornado", "Tsunami", "Earthquake", "Epidemic", "Flood",
    "Heat/Sun Stroke", "Landslide", "Lightning", "Torrential Rain", "Forest Fire", "Causes other than above",
    "Total"
]
age_groups = ["14 and Above-Below 18 years - Male", "14 and Above-Below 18 years - Female", "14 and Above-Below 18 years - Transgender", "14 and Above-Below 18 years - Total"]
data = np.array([
    [1, 0, 0, 1],
    [3, 4, 0, 7],
    [2, 1, 0, 3],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [49, 28, 0, 77],
    [0, 1, 0, 1],
    [21, 9, 0, 30],
    [156, 46, 0, 202],
    [4, 1, 0, 5],
    [0, 0, 0, 0],
    [20, 16, 0, 36],
    [256, 106, 0, 362]
])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Number of Cases by Cause and Age Group Below 14", fontsize=16)

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
ax.legend(loc="upper right", fontsize=10)
plt.tight_layout()

plt.show()
