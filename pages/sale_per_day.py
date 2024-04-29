import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from hemnet import get_hemnet_data

hemnet = get_hemnet_data()

new = hemnet['sale_date'].str.extract('')
