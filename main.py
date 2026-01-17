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
