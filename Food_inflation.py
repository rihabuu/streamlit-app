import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data (replace with the appropriate URL or filepath)
data_url = 'C:\Users\Zouitina Rihab\Desktop\Projet DV'
data = pd.read_csv(Monthly food Price Inflation Estimates by country.csv)

st.header('Inflation Visualization Project')
st.subheader('This page visualizes inflation rates for different countries over time.')

# 1. Pie Chart Visualization of Average Inflation per Country
avg_inflation = data.groupby('country')['Inflation'].mean().reset_index()
fig = px.pie(avg_inflation, names='country', values='Inflation', title='Average Inflation per Country')
st.plotly_chart(fig)

# 2. Line Plot Visualization for Inflation Over Time
country_choice = st.selectbox("Select a country to visualize its inflation over time:", data['country'].unique())
country_data = data[data['country'] == country_choice]
fig = px.line(country_data, x='date', y='Inflation', title=f"Inflation Over Time for {country_choice}")
st.plotly_chart(fig)

# 3. Histogram Visualization of Inflation Distribution
st.write("Distribution of Inflation Rates")
fig = px.histogram(data, x="Inflation", title="Distribution of Inflation Rates")
st.plotly_chart(fig)

# 4. (Any other visualizations you'd like to add based on your dataset)

st.caption('YOUR_NAME')
st.caption('Thank you for exploring the inflation data!')
