# Temporal Components: Extract year, month, week of the year, and day of the week from the date.
# Categorical Variables, Season: Winter, Spring, Summer, Fall.
# Is_Weekend: 1 if it's Saturday or Sunday, 0 otherwise.
# Quick Analysis:
# Group sales by month to identify seasonal patterns.
# Save the dataset with the new columns as Walmart_engineered.csv.


import pandas as pd
import matplotlib.pyplot as plt

# Clean data
df = pd.read_csv("data/Walmart_clean.csv", parse_dates=["Date"])

# Feature Engineering
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Week_of_Year"] = df["Date"].dt.isocalendar().week
df["Day_of_Week"] = df["Date"].dt.dayofweek  # 0=Monday, 6=Sunday


# Variable : season
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"


df["Season"] = df["Month"].apply(get_season)

# Variable: Is this weekend?
df["Is_Weekend"] = df["Day_of_Week"].isin([5, 6]).astype(int)

# Analisis, monthly sells
monthly_sales = df.groupby("Month")["Weekly_Sales"].mean()

# Export data
df.to_csv("data/Walmart_engineered.csv", index=False)
print("Data save in 'data/Walmart_engineered.csv'")

# Monthly Sales Visualization
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="bar", color="skyblue")
plt.title("Average Sales per Month (2010–2012)")
plt.xlabel("Month")
plt.ylabel("Average Sales (USD)")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.savefig("results/monthly_sales.png")  # Save graphic
plt.show()
