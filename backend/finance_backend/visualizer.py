# from alpaca: get a select box of all the possible stocks and then 
# make a df with the selected stocks and the date range and then plot it
# could use cache to store recently used stocks
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from typing import  List
from st_aggrid import AgGrid
from main import get_yfinance_data

st.title("Asset Visualizer")

wanted_symbols = ["AAPL", "MSFT", "NVDA", "META", "TSLA", "^GSPC", "BTC-USD","ETH-USD", "SOL-USD"]
symbol_data_dict = get_yfinance_data(wanted_symbols)
symbol_selection = st.selectbox("Pick your asset", wanted_symbols)
plot = px.line(symbol_data_dict[symbol_selection], x="Date", y="Close", labels={"Close": f"{symbol_selection} Price (USD)"})
st.plotly_chart(plot, use_container_width = True)

