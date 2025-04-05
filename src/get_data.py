import os
import yfinance as yf

def fetch_and_save_data():
    # Fetch S&P 500 data for the last 5 years
    sp500 = yf.Ticker("^GSPC")
    sp500_data = sp500.history(period="5y")

    # Ensure the data directory exists
    data_dir = "../data"
    os.makedirs(data_dir, exist_ok=True)

    # Save to CSV file
    file_path = os.path.join(data_dir, "sp500_5_years_data.csv")
    sp500_data.to_csv(file_path)

    print(f"Data saved to {file_path}")

# Run the function
fetch_and_save_data()