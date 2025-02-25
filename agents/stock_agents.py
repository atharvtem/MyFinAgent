from autogen import AssistantAgent, UserProxyAgent
from agents.config import config_list

class StockAgents:
    def __init__(self):
        self.user_proxy = UserProxyAgent(
            name="User_Proxy",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
        )
        
        self.data_fetcher = AssistantAgent(
            name="Data_Fetcher",
            llm_config={"config_list": config_list},
            system_message="You fetch stock data using yfinance API."
        )
        
        self.technical_analyst = AssistantAgent(
            name="Technical_Analyst",
            llm_config={"config_list": config_list},
            system_message="You analyze technical indicators like SMA, RSI, and MACD."
        )