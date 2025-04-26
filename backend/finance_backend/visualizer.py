# from alpaca: get a select box of all the possible stocks and then 
# make a df with the selected stocks and the date range and then plot it
# could use cache to store recently used stocks
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from typing import  List
from app import WANTED_SYMBOLS, data_frame_dict
from optionspage import expected_price_modelling

st.title("Asset Visualizer")    

st.header("Historical Visualizer")
symbol_selection = st.selectbox("Pick your asset", WANTED_SYMBOLS)
plot = px.line(data_frame_dict[symbol_selection], x="Date", y="Close", labels={"Close": f"{symbol_selection} Price (USD)"})
st.plotly_chart(plot, use_container_width = True)

st.header("Price Prediction Visualizer")
select = st.selectbox("Choose your asset", WANTED_SYMBOLS)
df = data_frame_dict[select]
price_model_df = expected_price_modelling(df=df)
plot = px.line(price_model_df, x="Date", y="Price")
st.plotly_chart(plot, True)



