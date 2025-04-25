from sklearn.linear_model import LinearRegression
import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st


# build a random forest regression model to predict percentage change in the
# next day. Use historical data from Yahoo Finance to train the model. Choose 
# few stocks for this model

wanted_symbols = ["AAPL", "MSFT", "NVDA", "META", "TSLA", "^GSPC", "BTC-USD","ETH-USD", "SOL-USD"]

@st.cache_data
def get_yfinance_data(symbols):

    stock_history = lambda x: yf.Ticker(x).history("max")
    data_frame_dict = {}

    for symbol in symbols:
        data_frame_dict[symbol] = stock_history(symbol)

        if "Volume" and "Stock Splits" and "Dividends" in stock_history(symbol):        
            data_frame_dict[symbol] = data_frame_dict[symbol].drop(["Volume", "Stock Splits", "Dividends"], axis = 1) 
        
        data_frame_dict[symbol]["Percent_Change"] = data_frame_dict[symbol]["Close"].pct_change() * 100
        data_frame_dict[symbol].index = data_frame_dict[symbol].index.date
        data_frame_dict[symbol]["Date"] = data_frame_dict[symbol].index

    return data_frame_dict







