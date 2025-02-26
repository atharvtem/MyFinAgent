from agents.stock_agents import StockAgents

agents = StockAgents()
agents.user_proxy.initiate_chat(
    agents.data_fetcher,
    message="Fetch stock data for TSLA for the last 6 months."
)