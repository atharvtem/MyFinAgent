import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_stock_plotly(data: dict, ticker: str):
    """Plot stock price, SMA, and RSI."""
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

    # Price and SMA plot
    fig.add_trace(
        go.Scatter(x=data["dates"], y=data["prices"], name="Closing Price"),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=data["dates"], y=data["sma"], name="20-Day SMA"),
        row=1, col=1
    )

    # RSI plot
    fig.add_trace(
        go.Scatter(x=data["dates"], y=data["rsi"], name="RSI"),
        row=2, col=1
    )

    fig.update_layout(
        height=600,
        title_text=f"{ticker} Technical Analysis",
        showlegend=True
    )
    return fig