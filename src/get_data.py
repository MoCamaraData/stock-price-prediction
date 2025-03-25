import yfinance as yf
import pandas as pd
import os

# Define the stock symbol and date range
stock_symbol = "AAPL"  # Change this as needed
start_date = "2010-01-01"
end_date = "2023-01-01"

# Download stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date, progress=False)

# Ensure 'data' folder exists
data_folder = "../data"
os.makedirs(data_folder, exist_ok=True)

# Save to CSV
csv_path = os.path.join(data_folder, f"{stock_symbol}_stock_data.csv")
stock_data.to_csv(csv_path)

print(f"Data saved to {csv_path}")
print(stock_data.head())
