from pyexpat import model
import alpaca_trade_api
from pricing.GBM import model_price
from app import data_frame_dict, WANTED_SYMBOLS
import streamlit as st
import plotly.express as px


"""
This page allows one to appropriately price options using Black-Scholes.
The future prices of the asset are determined using a modified version of
GBM which includes getting data from LLM to give a valid drift and
volatility for the asset price

"""

# get the first day and price on that day
selection = st.selectbox("Choose your asset", WANTED_SYMBOLS)
chosen_df = data_frame_dict[selection]

def expected_price_modelling(df):
    today_price = df.iloc[-1, 3]
    today_date = df.iloc[-1, -1]

    price_model_df = model_price(today_price, today_date, 0.2477, 0.2261)
    return price_model_df

price_model_df = expected_price_modelling(chosen_df)
plot = px.line(price_model_df, x="Date", y="Price")
st.plotly_chart(plot, True)

