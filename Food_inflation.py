import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

data = pd.read_csv("data_FI.csv")
st.write(data.head())
