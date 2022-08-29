import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App ***(GOOGL)***.

Shown are the stock ***closing price*** and ***volume*** of Google!

""")
# Definition of the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices
tickerDf = tickerData.history(period='id', start='2012-8-30', end='2022-8-28')

# Open        High        Low Close   Volume  Dividends   Stock splits

st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume price
""")
st.line_chart(tickerDf.Volume)
