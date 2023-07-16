import numpy as np
import matplotlib.pyplot as plt

# Data
causes = [
    "Avalanche", "Exposure to cold", "Cyclone", "Tornado", "Tsunami", "Earthquake", "Epidemic", "Flood",
    "Heat/Sun Stroke", "Landslide", "Lightning", "Torrential Rain", "Forest Fire", "Causes other than above",
    "Total"
]
age_groups = ["18 and Above-Below 30 years - Male", "18 and Above-Below 30 years - Female", "18 and Above-Below 30 years - Transgender", "18 and Above-Below 30 years - Total"]
data = np.array([
    [3, 0, 0, 3],
    [60, 7, 0, 67],
    [29, 2, 0, 31],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [112, 23, 0, 135],
    [28, 8, 0, 36],
    [61, 29, 0, 90],
    [508, 153, 0, 661],
    [7, 2, 0, 9],
    [5, 0, 0, 5],
    [111, 39, 0, 150],
    [924, 263, 0, 1187]
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
