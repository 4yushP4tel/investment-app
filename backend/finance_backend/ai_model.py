from tracemalloc import start
from sklearn.linear_model import LogisticRegression
import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st
from typing import List
from app import get_yfinance_data, WANTED_SYMBOLS
from google import genai


# build a random forest regression model to predict percentage change in the
# next day. Use historical data from Yahoo Finance to train the model. Choose 
# few stocks for this model. Use both the random forest and gemini 2.5 pro to predict if the
# price will end up jumping or not. Check if there are active trades and buy/sell
# accordingly

st.title("AI Model")

def random_forest():
    pass

def gemini_support():
    sample_prompt = f"""
        you are a financial analyst who helps to predict the market regime for specific assets. You will help me predict the movement in price for different assets. This will be done on a price movement scale from -5 to 5. The movement of the price is said to be over a short period of time. Say a period of 1 to 2 weeks.

        * -5 showing a strong decrease in price.
        * 0 showing a neutral movement in price.
        * 5 showing strong increase in price.

        For the following asset symbols, you will give me the corresponding price movement scale value. The output should be in a python Dictionary type of data structure. Do not give any explanation for the output, just give me the dictionary. Use news data from all over the planet and past price data to make your decisions. 

        Here is the list of asset symbols:

        {WANTED_SYMBOLS}

    """
    return sample_prompt

this = gemini_support()
this











