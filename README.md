# PriceInsight Data Analysis

**PriceInsight** is a small Python project that analyzes product price changes from a CSV dataset.  
It calculates absolute and percentage changes in price, identifies the smallest and largest price changes, and visualizes the results in a bar chart.  

This project is ideal for practicing basic data cleaning, manipulation, and visualization using **Pandas**, **NumPy**, and **Matplotlib**.  

---

## Features

- Loads raw product pricing data from a CSV file.  
- Cleans the data and converts price columns to numeric values.  
- Calculates:
  - Absolute price change (`price_change`)  
  - Percentage change (`percent_change`)  
  - Average price (`mean_price`)  
- Identifies the smallest and largest price changes.  
- Saves cleaned data to a new CSV file.  
- Creates a bar chart of price changes per product, with color-coded trends.  

---

## Requirements

- Python 3.7 or higher  
- Pandas  
- NumPy  
- Matplotlib