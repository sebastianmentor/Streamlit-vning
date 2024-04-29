import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from hemnet import get_hemnet_data

sales_data = get_hemnet_data()

st.markdown(
    """ # Slutpris
    """)
fig = px.histogram(sales_data, x='final_price')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit")
with tab2:
    st.plotly_chart(fig, theme=None)

st.markdown(
    """ # Antal rum
    """)
fig = px.histogram(sales_data, x='rooms')
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit")
with tab2:
    st.plotly_chart(fig, theme=None)