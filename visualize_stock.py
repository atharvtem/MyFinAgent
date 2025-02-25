import matplotlib.pyplot as plt
import plotly.graph_objects as go

def plot_stock_matplotlib(data, ticker):
    """Plots stock closing prices using Matplotlib."""
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data["Close"], label=f"{ticker} Closing Prices", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{ticker} Stock Price Trend")
    plt.legend()
    plt.grid()
    plt.show()

def plot_stock_plotly(data, ticker):
    """Creates an interactive stock chart using Plotly."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Closing Price"))
    fig.update_layout(title=f"{ticker} Stock Price Trend",
                      xaxis_title="Date",
                      yaxis_title="Price (USD)",
                      template="plotly_dark")
    fig.show()

def plot_stock_plotly(data, ticker):
    """Interactive Plotly chart with technical indicators."""
    fig = go.Figure()
    
    # Closing Price
    fig.add_trace(go.Scatter(
        x=data.index, y=data["Close"], 
        name="Closing Price", line=dict(color="blue"))
    )
    
    # SMA
    if "SMA_20" in data.columns:
        fig.add_trace(go.Scatter(
            x=data.index, y=data["SMA_20"], 
            name="20-Day SMA", line=dict(color="orange", dash="dot"))
        )
    
    # MACD
    if "MACD_12_26_9" in data.columns:
        fig.add_trace(go.Scatter(
            x=data.index, y=data["MACD_12_26_9"], 
            name="MACD", line=dict(color="green")),
            row=2, col=1
        )
        fig.add_trace(go.Scatter(
            x=data.index, y=data["MACDs_12_26_9"], 
            name="Signal Line", line=dict(color="red")),
            row=2, col=1
        )
    
    fig.update_layout(
        title=f"{ticker} Technical Analysis",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark",
        height=800
    )
    fig.show()
