# from alpaca: get a select box of all the possible stocks and then 
# make a df with the selected stocks and the date range and then plot it
# could use cache to store recently used stocks
import numpy as np
import pandas as pd
from alpaca.data.historical import CryptoHistoricalDataClient
import datetime
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import plotly.express as px
import streamlit as st
from st_aggrid import AgGrid

st.header("Price of different assets")

client = CryptoHistoricalDataClient()


# Creating request object
request_params = CryptoBarsRequest(
  symbol_or_symbols=["BTC/USD", "ETH/USD"],
  timeframe=TimeFrame.Day,
  start=datetime.datetime(2022, 9, 1),
  end=datetime.datetime(2024, 11, 3)
)

asset_bars = client.get_crypto_bars(request_params)


# Convert to dataframe
df = asset_bars.df

timestamp = df.index.get_level_values("timestamp")
df["timestamp"] = timestamp

# Select assets:
selected_asset = st.selectbox("Select asset", df.index.get_level_values("symbol").unique())
filtered_df = df[df.index.get_level_values("symbol") == selected_asset]
print(filtered_df)

# Plots

plot = px.line(filtered_df, x="timestamp", y = "close", title=f"{selected_asset} Price")
plot = st.plotly_chart(plot)

