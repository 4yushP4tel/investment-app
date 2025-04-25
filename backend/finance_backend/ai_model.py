from tracemalloc import start
from sklearn.linear_model import LogisticRegression
import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st
from typing import List
from main import get_yfinance_data


# build a random forest regression model to predict percentage change in the
# next day. Use historical data from Yahoo Finance to train the model. Choose 
# few stocks for this model

st.title("AI Model")

wanted_symbols = ["AAPL", "MSFT", "NVDA", "META", "TSLA", "^GSPC", "BTC-USD","ETH-USD", "SOL-USD"]
data = get_yfinance_data(wanted_symbols)









