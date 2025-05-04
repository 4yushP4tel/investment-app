from itertools import dropwhile
from pyexpat import model
import alpaca_trade_api
from pricing.GBM import model_price
from app import data_frame_dict, WANTED_SYMBOLS
import streamlit as st
import plotly.express as px
from ai_model import gemini_pricing_support


"""
This page allows one to appropriately price options using Black-Scholes.
The future prices of the asset are determined using a modified version of
GBM which includes getting data from LLM to give a valid drift and
volatility for the asset price

"""

# get the first day and price on that day
selection = st.selectbox("Choose your asset", WANTED_SYMBOLS)
chosen_df = data_frame_dict[selection]
asset_variable_dict = gemini_pricing_support()

def expected_price_modelling(df, selection):
    today_price = df.iloc[-1, 3]
    today_date = df.iloc[-1, -1]
    drift = asset_variable_dict[selection]["drift"]
    volatility = asset_variable_dict[selection]["volatility"]



    price_model_df = model_price(today_price, today_date, drift, volatility)
    return [price_model_df, drift, volatility]

price_model_df, drift, volatility = expected_price_modelling(chosen_df, selection)
plot = px.line(price_model_df, x="Date", y="Price")

st.header("Price Prediction Over One Year")
st.button("Recompute Price Prediction")
st.plotly_chart(plot, True)
st.write(f"Expected Drift: {drift}")
st.write(f"Expected Volatility: {volatility}")

def price_option(expiry_date, asset, ):
    """
    
    """
    pass

