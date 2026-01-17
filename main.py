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
