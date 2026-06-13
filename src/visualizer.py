import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("output", exist_ok=True)

data = {
    "Warehouse": ["W1", "W1", "W2", "W2", "W3", "W3"],
    "Retailer": ["R1", "R4", "R2", "R4", "R3", "R4"],
    "Units": [600, 400, 1100, 100, 700, 100]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,5))
sns.barplot(data=df, x="Warehouse", y="Units")
plt.title("Distribution by Warehouse")
plt.savefig("output/cost_analysis.png")
plt.close()

pivot = df.pivot_table(
    values="Units",
    index="Warehouse",
    columns="Retailer",
    fill_value=0
)

plt.figure(figsize=(8,5))
sns.heatmap(pivot, annot=True, cmap="Blues")
plt.title("Distribution Heatmap")
plt.savefig("output/distribution_heatmap.png")
plt.close()

print("Graphs saved successfully")