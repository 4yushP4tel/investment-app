# from alpaca: get a select box of all the possible stocks and then 
# make a df with the selected stocks and the date range and then plot it
# could use cache to store recently used stocks
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from typing import  List
from st_aggrid import AgGrid
from app import get_yfinance_data, WANTED_SYMBOLS

st.title("Asset Visualizer")

symbol_data_dict = get_yfinance_data(WANTED_SYMBOLS)
symbol_selection = st.selectbox("Pick your asset", WANTED_SYMBOLS)
plot = px.line(symbol_data_dict[symbol_selection], x="Date", y="Close", labels={"Close": f"{symbol_selection} Price (USD)"})
st.plotly_chart(plot, use_container_width = True)

