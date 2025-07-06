# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
try:
    df = pd.read_csv("data/Walmart.csv")
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")

# Initial exploration
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset information (structure and data types):")
print(df.info())

print("\nDescriptive statistics (numerical):")
print(df.describe())

# Key columns analysis
print("\nAvailable columns:")
print(df.columns.tolist())

# Quick visualizations
plt.figure(figsize=(12, 6))

# Boxplot of Weekly_Sales (to detect outliers)
plt.subplot(1, 2, 1)
plt.boxplot(df["Weekly_Sales"])
plt.title("Weekly Sales Distribution")
plt.ylabel("Sales (USD)")

# Histogram of Weekly_Sales
plt.subplot(1, 2, 2)
plt.hist(df["Weekly_Sales"], bins=30, color="skyblue", edgecolor="black")
plt.title("Weekly Sales Frequency")
plt.xlabel("Sales (USD)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Sales per store analysis
print("\n🛒 Number of records per store:")
print(df["Store"].value_counts().sort_index())

# Initial relationship
plt.figure(figsize=(8, 5))
plt.scatter(df["Temperature"], df["Weekly_Sales"], alpha=0.5)
plt.ylabel("Weekly Sales (USD)")
plt.grid(True)
plt.show()
