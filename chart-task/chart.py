import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

data = pd.DataFrame({
    "category": np.repeat(["A", "B", "C"], 50),
    "value": np.concatenate([
        np.random.normal(10, 2, 50),
        np.random.normal(15, 3, 50),
        np.random.normal(20, 4, 50),
    ])
})

# 512px x 512px exactly
fig = plt.figure(figsize=(5.12, 5.12), dpi=100)
ax = plt.gca()

sns.boxplot(data=data, x="category", y="value", ax=ax)

ax.set_title("Seaborn Boxplot Example")
ax.set_xlabel("Category")
ax.set_ylabel("Value")

# DO NOT use bbox_inches or tight_layout (they change size)
plt.savefig("chart.png", dpi=100)
plt.close()
