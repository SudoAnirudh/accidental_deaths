import numpy as np
import matplotlib.pyplot as plt

# Data
causes = [
    "Avalanche", "Exposure to cold", "Cyclone", "Tornado", "Tsunami", "Earthquake", "Epidemic", "Flood",
    "Heat/Sun Stroke", "Landslide", "Lightning", "Torrential Rain", "Forest Fire", "Causes other than above",
    "Total"
]
age_groups = ["30 and Above-Below 45 years - Male", "30 and Above-Below 45 years - Female", "30 and Above-Below 45 years - Transgender", "30 and Above-Below 45 years - Total"]
data = np.array([
    [0, 1, 0, 1],
    [134, 14, 0, 148],
    [48, 0, 0, 48],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [83, 25, 0, 108],
    [76, 17, 0, 93],
    [69, 37, 0, 106],
    [725, 221, 0, 946],
    [14, 7, 0, 21],
    [3, 5, 0, 8],
    [174, 53, 1, 228],
    [1326, 381, 1, 1708]
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
