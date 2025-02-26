from fetch_stock import fetch_stock_data
from visualizations.visualize_stock import plot_stock_matplotlib, plot_stock_plotly

ticker = "AAPL"  # Apple stock
data = fetch_stock_data(ticker, period="6mo")

# Matplotlib static plot
plot_stock_matplotlib(data, ticker)

# Plotly interactive chart
plot_stock_plotly(data, ticker)
