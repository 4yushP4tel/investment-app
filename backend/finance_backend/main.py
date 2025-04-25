import streamlit as st

visualizer = st.Page("visualizer.py", title="Visualizer", icon="📊")
correlation = st.Page("correlation.py", title="Correlation", icon="📈")
trader = st.Page("trade.py", title="Trader", icon="💰")
ai_model = st.Page("ai_model.py", title="AI_model", icon="🤖")

pages = st.navigation(pages=[visualizer, correlation, trader, ai_model])
pages.run()