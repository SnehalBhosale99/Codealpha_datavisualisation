import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample dataset
df = sns.load_dataset("iris")

# Create a figure with 3 subplots (1 row, 3 columns)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Histogram
sns.histplot(df['sepal_length'], kde=True, bins=20, ax=axes[0])
axes[0].set_title("Distribution of Sepal Length")

# 2. Scatter Plot
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, ax=axes[1])
axes[1].set_title("Sepal Length vs Petal Length")

# 3. Box Plot
sns.boxplot(x="species", y="sepal_width", data=df, ax=axes[2])
axes[2].set_title("Sepal Width by Species")

# Adjust layout
plt.tight_layout()

# Save as single image
plt.savefig("iris_visualizations.png")

# Show combined image
plt.show()

