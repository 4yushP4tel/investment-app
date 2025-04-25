import streamlit as st
from dotenv import load_dotenv
import os
import alpaca_trade_api
from alpaca.data.historical import CryptoHistoricalDataClient
import datetime
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame


#get environment variables
load_dotenv()
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL_ALPACA = os.getenv("BASE_URL")

st.write("trade")

"""
This will allow me to make algorthmic trades, based on correlation, the ai model
and factors like placing level trades. This will be implemented using the alpaca api
"""

class Trader:
    def __init__(self):
        pass

    def get_active_trades(self):
        pass

    def get_orders(self):
        pass

    def get_ai_model_info(self, asset):
        pass

    def place_trade(self):
        pass

    

    
