import pandas as pd
import yfinance as yf
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_and_preprocess_data(ticker, start_date, end_date):
    # Fetch historical data
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Display the DataFrame before dropping missing values
    print("Before dropping missing values:")
    print(stock_data.head(10))

    # Handle missing values by removing missing values 'NaN'
    stock_data.dropna(inplace=True)

    # Display the DataFrame after dropping missing values
    print("\nAfter dropping missing values:")
    print(stock_data.head(10))
    
    # Calculate additional metrics
    stock_data['50_MA'] = stock_data['Adj Close'].rolling(window=50).mean()
    stock_data['200_MA'] = stock_data['Adj Close'].rolling(window=200).mean()


    # Get today's date and format it
    today_date = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save the preprocessed data to a CSV file
    stock_data.to_csv(f"{ticker}_preprocessed_{today_date}.csv")
    
    return stock_data

# fetching Apple Inc.'s stock for the period "2020-01-01", "2023-01-01"
data = fetch_and_preprocess_data("AAPL", "2020-01-01", "2023-01-01")
print(data.head())
