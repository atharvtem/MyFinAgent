import ta
import langgraph.graph as lg

def analyze_technical_indicators(inputs):
    df = inputs["stock_data"]
    df["SMA"] = df["Close"].rolling(window=14).mean()
    df["RSI"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    return {"technical_data": df}

import yfinance as yf
def fetch_stock_data(inputs):
    """Fetch stock data using yfinance."""
    ticker = inputs["ticker"]
    period = inputs["period"]
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return {"stock_data": data}
