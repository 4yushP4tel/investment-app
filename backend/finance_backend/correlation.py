from csv import Error
from enum import auto
from sqlite3 import OperationalError
from typing import List, Optional
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import numpy as np
from app import get_yfinance_data, WANTED_SYMBOLS

data_dict = get_yfinance_data(WANTED_SYMBOLS)

st.title("Correlation and Autocorrelation Detection")

st.header("Correlation Detection")


@st.cache_data
def find_correlation(symbol1: str, symbol2: str, timeframe: Optional[List] = None):
    """
        Creates df with percent change of both assets.
        Both assets must be different
    """
    try:
        df1 = data_dict[symbol1]
        df2 = data_dict[symbol2]
        df = pd.merge(df1, df2, how='inner', on="Date",
                    suffixes=(f"_{symbol1}",f"_{symbol2}",
                    ))
        df = df[(df[f"Percent_Change_{symbol1}"].notna()) & (df[f"Percent_Change_{symbol1}"] != 0)]
        df = df[(df[f"Percent_Change_{symbol2}"].notna()) & (df[f"Percent_Change_{symbol2}"] != 0)]
        df = df[["Date", f"Percent_Change_{symbol1}", f"Percent_Change_{symbol2}"]]

        #using pearson since we are looking at the percentage change not price
        corr = df[[f"Percent_Change_{symbol1}", f"Percent_Change_{symbol2}"]].corr(method='pearson')
        return [df, corr]

    
    except Exception as e:
        st.markdown(f"Both assets must be different, {e}")

    
#select assets and show correlation
asset1 = st.selectbox("Asset1: ", WANTED_SYMBOLS)
new_symbols = WANTED_SYMBOLS
new_symbols.remove(asset1)
asset2 = st.selectbox("Asset2: ", new_symbols)
df, corr_matrix = find_correlation(asset1, asset2)
st.subheader("Correlation Matrix")
corr_matrix
dates = df["Date"].to_list()

st.header("Autocorrelation Detection")
@st.cache_data
def find_autocorrelation(symbol: str, lag : int):
    # try:
    df = data_dict[symbol]
    df = df[["Date", "Percent_Change", "Close"]]
    df = df[(df["Percent_Change"].notna()) & (df[f"Percent_Change"] != 0)]
    autocorr_change = np.round(df["Percent_Change"].autocorr(lag=lag), 4)
    autocorr_price = np.round(df["Close"].autocorr(lag=lag), 4)
    return_df = pd.DataFrame({f"Autocorrelation of price change for {symbol} with lag of {lag} day": autocorr_change,
                              f"Autocorrelation of price for {symbol} with lag of {lag} day": autocorr_price
                              }, index=["Coefficient"])
    # except Exception as e:
    #     st.markdown("Error in autocorrelation")
    return return_df


#choose lag and symbol and find autocorrelation
asset = st.selectbox("Asset:", WANTED_SYMBOLS)
lag = st.slider("Lag", 1, 365)

df = find_autocorrelation(asset, lag)
st.table(df)




