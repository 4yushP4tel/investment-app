from typing import List
import streamlit as st
import yfinance as yf

WANTED_SYMBOLS = ["AAPL", "MSFT", "NVDA", "META", "TSLA", "^GSPC", "BTC-USD","ETH-USD", "SOL-USD"]


@st.cache_data
def get_yfinance_data(symbols: List):

    stock_history = lambda x: yf.Ticker(x).history("max")
    data_frame_dict = {}

    for symbol in symbols:
        data_frame_dict[symbol] = stock_history(symbol)

        if "Volume" and "Stock Splits" and "Dividends" in stock_history(symbol):        
            data_frame_dict[symbol] = data_frame_dict[symbol].drop(["Volume", "Stock Splits", "Dividends"], axis = 1) 
        
        data_frame_dict[symbol]["Percent_Change"] = data_frame_dict[symbol]["Close"].pct_change() * 100
        data_frame_dict[symbol]["Date"] = data_frame_dict[symbol].index.date
        data_frame_dict[symbol].index.name = "Time"


    return data_frame_dict

data_frame_dict = get_yfinance_data(WANTED_SYMBOLS)
visualizer = st.Page("visualizer.py", title="Visualizer", icon="📊")
correlation = st.Page("correlation.py", title="Correlation", icon="📈")
trader = st.Page("trade.py", title="Trader", icon="💰")
ai_model = st.Page("ai_model.py", title="AI Model", icon="🤖")
options = st.Page("optionspage.py", title="Options Pricing", icon="📊")
regimes = st.Page("market_regimes", title="Market Regimes", icon="🐂🐻")

pages = st.navigation(pages=[visualizer, correlation, trader, ai_model, options, regimes])
pages.run()