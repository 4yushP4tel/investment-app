from typing import List
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
from main import get_yfinance_data

wanted_symbols = ["AAPL", "MSFT", "NVDA", "META", "TSLA", "^GSPC", "BTC-USD","ETH-USD", "SOL-USD"]
data_dict = get_yfinance_data(wanted_symbols)

st.title("Correlation and Autocorrelation Detection")

st.header("Correlation Detection")

@st.cache_data
def find_correlation(symbol1: str, symbol2: str, ):
    df1 = data_dict[symbol1]
    df2 = data_dict[symbol2]
    df = pd.merge(df1, df2, how='inner', on="Date",
                  suffixes=(f"_{symbol1}",f"_{symbol2}",
                  ))
    df = df[(df[f"Percent_Change_{symbol1}"].notna()) & (df[f"Percent_Change_{symbol1}"] != 0)]
    df = df[(df[f"Percent_Change_{symbol2}"].notna()) & (df[f"Percent_Change_{symbol2}"] != 0)]
    df = df[["Date", f"Percent_Change_{symbol1}", f"Percent_Change_{symbol2}"]]

    return df

df = find_correlation("AAPL", "MSFT")
AgGrid(df)


st.header("Autocorrelation Detection")
@st.cache_data
def find_autocorrelation(symbol: str, timespan: List[str]):
    pass



