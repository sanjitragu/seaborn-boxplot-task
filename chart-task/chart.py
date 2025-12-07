import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Make the output reproducible
np.random.seed(42)

# Create some example data
data = pd.DataFrame({
    "category": np.repeat(["A", "B", "C"], 50),
    "value": np.concatenate([
        np.random.normal(loc=10, scale=2, size=50),
        np.random.normal(loc=15, scale=3, size=50),
        np.random.normal(loc=20, scale=4, size=50),
    ])
})

# Create a figure that will be exactly 512x512 pixels
# size (inches) * dpi = pixels
# 5.12 inches * 100 dpi = 512 pixels
fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=100)

# Create a Seaborn boxplot
sns.boxplot(data=data, x="category", y="value", ax=ax)

ax.set_title("Example Seaborn Boxplot")
ax.set_xlabel("Category")
ax.set_ylabel("Value")

# Save the chart as exactly 512x512 PNG in the same folder
fig.savefig("chart.png", dpi=100, bbox_inches="tight")

plt.close(fig)

