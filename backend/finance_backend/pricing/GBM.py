from datetime import date
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


# General brownian motion, Wiener Process
#252 business days in year
steps = 252
time_increment = 1/steps
time_span = lambda start: pd.date_range(start, periods=steps, freq="B")

t = np.linspace(0, 1, steps)
brownian_motion = lambda : np.cumsum(np.random.normal(0, np.sqrt(time_increment), size=steps))

# Modelling Stock Price Future for certain stock

st.cache_data
def model_price(price_today, start_date, drift, volatility):
    time_span_index = pd.Index(time_span(start_date), name="Dates")
    prices = price_today* np.e**(drift - 0.5*(volatility**2)*t + volatility*brownian_motion())
    
    prices_df = pd.DataFrame({"Price": prices, "Date": time_span(start_date)}, index=time_span_index)
    return prices_df

    
# returns after doing the same approximation 100 times


        


