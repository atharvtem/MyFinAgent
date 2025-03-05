import ta

def analyze_technical_indicators(inputs):
    """Add SMA & RSI to stock data"""
    df = inputs["stock_data"]
    df["SMA"] = df["Close"].rolling(window=14).mean()
    df["RSI"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    return {"technical_data": df}
