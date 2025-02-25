import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "1mo", interval: str = "1d"):
    """
    Fetch historical stock data for a given ticker.
    
    Args:
    ticker (str): Stock symbol (e.g., "AAPL" for Apple).
    period (str): Time period (e.g., "1mo", "6mo", "1y").
    interval (str): Data interval (e.g., "1d", "1h").
    
    Returns:
    pd.DataFrame: Stock price data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    
    if data.empty:
        raise ValueError(f"No data found for {ticker}. Check if the ticker is correct.")
    
    return data

# Example usage
if __name__ == "__main__":
    ticker = "TSLA"  # Tesla stock
    data = fetch_stock_data(ticker, period="3mo")
    print(data.head())
