import os
import sys

# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to sys.path
sys.path.insert(0, parent_dir)

# Now you can import fetch_stock
from fetch_stock import fetch_stock_news

ticker = "MSFT"  # Test with Apple stock
news = fetch_stock_news(ticker)

if news:
    print(f"Top 5 news headlines for {ticker}:")
    for item in news[:5]:
        print(f"Title: {item.get('title', 'No title available')}")
        print(f"Source: {item.get('publisher', 'No publisher available')}")
        print("---")
else:
    print("No news available.")