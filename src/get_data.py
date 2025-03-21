import yfinance as yf
import pandas as pd

# Define the stock symbol and date range
stock_symbol = "AAPL"  # Change this to any stock (e.g., TSLA, GOOG)
start_date = "2010-01-01"
end_date = "2023-01-01"

# Download stock data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Save to CSV in the data folder
csv_path = f"../data/{stock_symbol}_stock_data.csv"
stock_data.to_csv(csv_path)

print(f"Data saved to {csv_path}")
print(stock_data.head())

