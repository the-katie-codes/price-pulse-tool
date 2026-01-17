"""
PricePulse Analysis
-------------------
This script analyzes price changes of products from a CSV dataset.
It calculates absolute and percentage price changes, average price,
and trends, then saves cleaned data and visualizes the changes in a bar chart.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Step 1: Load Data
# -------------------------
data = pd.read_csv('data/pricepulse_sample_data.csv')

# -------------------------
# Step 2: Clean & Convert Prices
# -------------------------
data["old_price"] = pd.to_numeric(data["old_price"], errors="coerce")
data["new_price"] = pd.to_numeric(data["new_price"], errors="coerce")

# -------------------------
# Step 3: Calculate Metrics
# -------------------------

# Calculate price changes
data["price_change"] = round(data["new_price"] - data["old_price"], 2)

# Calculate price change in percentage
data["percent_change"] = np.where(
    data["old_price"] != 0,
    data["price_change"] / data["old_price"] * 100,
    np.nan
)

# Calculate mean price
data["mean_price"] = round((data["old_price"] + data["new_price"]) / 2, 2)

# -------------------------
# Step 4: Summary Stats
# -------------------------

min_price = round(data["price_change"].min(skipna=True), 2)
max_price = round(data["price_change"].max(skipna=True), 2)

print(f"Smallest price change: {min_price}")
print(f"Biggest price change: {max_price}")

# -------------------------
# Step 5: Save Cleaned Data
# -------------------------
data.to_csv("data/pricepulse_clean_data.csv", index=False)

# -------------------------
# Step 6: Visualization
# -------------------------

# Prepare data for chart
chart_data = data.dropna(subset=["price_change"])

# Set x and y axis
x_axis = chart_data["product"]
y_axis = chart_data["price_change"]

# Create bar chart
plt.bar(x_axis, y_axis)

# Add labels and title
plt.xlabel("Product name")
plt.ylabel("Price Change (€)")
plt.title("Price Change per Product")
plt.xticks(rotation=90)

# Display the chart
plt.show()
