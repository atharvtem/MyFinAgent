import pandas as pd
import pandas_ta as ta

def calculate_sma(data, window=20):
    """Calculate Simple Moving Average (SMA)."""
    data[f"SMA_{window}"] = ta.sma(data["Close"], length=window)
    return data

def calculate_rsi(data, window=14):
    """Calculate Relative Strength Index (RSI)."""
    data["RSI"] = ta.rsi(data["Close"], length=window)
    return data

def calculate_macd(data, fast=12, slow=26, signal=9):
    """Calculate MACD and Signal Line."""
    macd = ta.macd(data["Close"], fast=fast, slow=slow, signal=signal)
    data = pd.concat([data, macd], axis=1)
    return data

def add_technical_indicators(data):
    """Add all technical indicators to the DataFrame."""
    data = calculate_sma(data, window=20)
    data = calculate_rsi(data, window=14)
    data = calculate_macd(data)
    return data

def generate_technical_summary(data):
    """Generate a summary of technical indicators."""
    summary = {
        "RSI": data["RSI"].iloc[-1],  # Latest RSI value
        "MACD": data["MACD_12_26_9"].iloc[-1],  # Latest MACD value
        "Signal": data["MACDs_12_26_9"].iloc[-1],  # Latest Signal value
    }
    return summary