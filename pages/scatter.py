import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from hemnet import get_hemnet_data

hemnet_data = get_hemnet_data()

st.header('')

fig = px.scatter(
    hemnet_data,
    x="area",
    y="final_price",
    hover_name="commune",
    size_max=60,
)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)