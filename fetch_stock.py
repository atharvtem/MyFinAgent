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


import requests

def fetch_stock_news(ticker):
    """Fetch financial news headlines using NewsAPI."""
    api_key = "ca1992cd8d5b487f9185d0a8a5f77eb1"  
    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={api_key}&language=en&sortBy=publishedAt"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = response.json().get("articles", [])
            return news
        else:
            print(f"Error fetching news: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    ticker = "NVDA"  # Tesla stock
    data = fetch_stock_data(ticker, period="3mo")
    news = fetch_stock_news(ticker)
    print(data.head())
    for item in news[:5]:
        print(f"Title: {item.get('title')}")
        print(f"Source: {item.get('publisher')}")
