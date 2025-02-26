import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_stock_plotly(data, ticker):
    """Creates an interactive stock chart using Plotly with subplots."""
    # Create a subplot grid
    fig = make_subplots(
        rows=2, cols=1,  # 2 rows, 1 column
        shared_xaxes=True,
        vertical_spacing=0.1,
        subplot_titles=(f"{ticker} Stock Price Trend", "MACD")
    )

    # Add Closing Price trace
    fig.add_trace(
        go.Scatter(
            x=data.index, y=data["Close"],
            name="Closing Price",
            line=dict(color="blue")
        ),
        row=1, col=1  # Add to the first subplot
    )

    # Add SMA trace (if available)
    if "SMA_20" in data.columns:
        fig.add_trace(
            go.Scatter(
                x=data.index, y=data["SMA_20"],
                name="20-Day SMA",
                line=dict(color="orange", dash="dot")
            ),
            row=1, col=1  # Add to the first subplot
        )

    # Add MACD traces (if available)
    if "MACD_12_26_9" in data.columns:
        fig.add_trace(
            go.Scatter(
                x=data.index, y=data["MACD_12_26_9"],
                name="MACD",
                line=dict(color="green")
            ),
            row=2, col=1  # Add to the second subplot
        )
        fig.add_trace(
            go.Scatter(
                x=data.index, y=data["MACDs_12_26_9"],
                name="Signal Line",
                line=dict(color="red")
            ),
            row=2, col=1  # Add to the second subplot
        )

    # Update layout
    fig.update_layout(
        title=f"{ticker} Technical Analysis",
        height=800,
        showlegend=True,
        template="plotly_dark"
    )

    # Update y-axis titles
    fig.update_yaxes(title_text="Price (USD)", row=1, col=1)
    fig.update_yaxes(title_text="MACD", row=2, col=1)

    return fig