from tracemalloc import start
from turtle import mode
from sklearn.linear_model import LogisticRegression
import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st
from typing import List
from app import get_yfinance_data, WANTED_SYMBOLS
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import json

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)


# build a random forest regression model to predict percentage change in the
# next day. Use historical data from Yahoo Finance to train the model. Choose 
# few stocks for this model. Use both the random forest and gemini 2.5 pro to predict if the
# price will end up jumping or not. Check if there are active trades and buy/sell
# accordingly

st.title("AI Model")

def random_forest():
    pass


@st.cache_data
def gemini_pricing_support():

    prompt = """
        #Note all I want is a python dict of results, I do not want code, I do not want words explaining anything

        You are a financial analyst who will help me with making price predictions.
        You will help me find appropriate drift and volatility variables used in geometric brownian motion.
        Using data from different new sources, find these variables for the following list of assets:
        ["AAPL", "MSFT", "NVDA", "META", "TSLA", "^GSPC", "BTC-USD","ETH-USD", "SOL-USD"]

        Give me the variables in decimals (positive or negative values are both possible) and give me 
        the result in a nested python dictionary
        with the keys for each asset being its asset symbol and the key for the variables being
        drift and volatility.
        Find the results for me I do not want to know from where they come just make them for me
        Do not code this and do not show me the process of your thinking only give me the resulting dictionary
        of values. Also note that I am using the GBM model over a period of 252 days which represents the amount of
        trading days in the year
    """
        


    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt, 
        config = types.GenerateContentConfig(
            max_output_tokens=500,
            temperature=0.05
        )
    )

    # response_dict = json.loads(response.text)
    string_reponse = response.text
    cleaned_response = string_reponse.replace("\n", " ")
    cleaned_response = cleaned_response.replace("\t", " ")
    cleaned_response = cleaned_response.replace("python", "")
    cleaned_response = cleaned_response.replace("```", "")
    response_dict = json.loads(cleaned_response)
    return response_dict


def gemini_support_stock_trading():
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













