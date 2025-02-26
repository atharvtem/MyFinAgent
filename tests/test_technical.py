from fetch_stock import fetch_stock_data
from analysis.technical_analysis import add_technical_indicators
from visualizations.visualize_stock import plot_stock_plotly

# Fetch data
ticker = "MSFT"
data = fetch_stock_data(ticker, period="6mo")

# Add indicators
data = add_technical_indicators(data)

# Plot interactive chart
plot_stock_plotly(data, ticker)

print("Technical indicators added successfully!")