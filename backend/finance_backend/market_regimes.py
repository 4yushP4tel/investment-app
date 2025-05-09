import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as nums
import streamlit as st

st.title("Track and classify market regimes")
st.header("Trend: Bullish, Bearish or Sideways")
st.header("Volatility: Low or High")
