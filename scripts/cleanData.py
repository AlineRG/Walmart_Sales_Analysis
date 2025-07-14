import pandas as pd
import numpy as np
from datetime import datetime

# Download data
try:
    df = pd.read_csv("data/Walmart.csv")
    print("Data loaded successfully")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Convert 'Date' to datetime
try:
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
except ValueError:
    # Try alternative format if the first one fails
    try:
        df["Date"] = pd.to_datetime(df["Date"], format="%m-%d-%Y")
    except Exception as e:
        print(f"Error converting dates: {e}")
        exit()

# Handle outliers in 'Weekly_Sales'
Q1 = df["Weekly_Sales"].quantile(0.25)
Q3 = df["Weekly_Sales"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_clean = df[(df["Weekly_Sales"] >= lower_bound) & (df["Weekly_Sales"] <= upper_bound)]

# Validate logical ranges
df_clean = df_clean[
    (df_clean["Temperature"] >= -10)
    & (df_clean["Temperature"] <= 110)  # Reasonable range in °F
]

# Export clean data
try:
    df_clean.to_csv("data/Walmart_clean.csv", index=False)
    print("Clean data exported to 'data/Walmart_clean.csv'")

    # Summary of changes
    print(f"\n🔹 Original records: {len(df)}")
    print(f"🔹 Records after cleaning: {len(df_clean)}")
    print(f"🔹 Records removed: {len(df) - len(df_clean)}")
except Exception as e:
    print(f"Error exporting clean data: {e}")
