import numpy as np
import matplotlib.pyplot as plt

# Data
causes = [
    "Avalanche", "Exposure to cold", "Cyclone", "Tornado", "Tsunami", "Earthquake", "Epidemic", "Flood",
    "Heat/Sun Stroke", "Landslide", "Lightning", "Torrential Rain", "Forest Fire", "Causes other than above",
    "Total"
]
age_groups = ["45 and Above-Below 60 years - Male", "45 and Above-Below 60 years - Female", "45 and Above-Below 60 years - Transgender", "45 and Above-Below 60 years - Total"]
data = np.array([
    [1, 0, 0, 1],
    [171, 44, 0, 215],
    [19, 2, 0, 21],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [68, 42, 0, 110],
    [122, 18, 0, 140],
    [45, 23, 0, 68],
    [502, 140, 1, 643],
    [14, 4, 0, 18],
    [3, 3, 0, 6],
    [165, 50, 0, 215],
    [1110, 326, 1, 1437]
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
ax.legend(loc="upper right", fontsize=10)
plt.tight_layout()

plt.show()
