import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

data = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/5f71ba43-afc8-43a0-b306-dafe29940f9c', sep=';')
st.header('Visualization Project', divider='rainbow')
st.subheader('This page contains several visualizations of the distribution of various pathologies. Most of the graphics are based on level 1 pathologies.')

#1 Viz
st.write('Let\'s take a look at the distribution of level 1 pathologies')
fig = px.pie(data, names='patho_niv1', title='Distribution of patients managed by level 1 pathology')
st.plotly_chart(fig)

#2 viz
st.write("A closer look at this evolution over time")
patho_niv1 = st.selectbox("Choose a pathology :", data['patho_niv1'].unique(), key='niv1')
niv1_data = data[data['patho_niv1'] == patho_niv1]
combined_data = niv1_data[['annee', 'prev']].groupby('annee').mean()

plt.figure(figsize=(12, 6))
combined_data.plot()
plt.title(f"Evolution of the prevalence of {patho_niv1} over time")
plt.xlabel("Year")
plt.ylabel("Prevalence (%)")
st.pyplot(plt)

#3 Viz
st.write("What about the distribution of level 3 pathologies")
patho3 = st.selectbox('Choose a pathology', data['patho_niv3'].unique(), key='niv3')
data_patho3 = data[data['patho_niv3'] == patho3]

source = ColumnDataSource(data_patho3)
p = figure(title=f'Evolution of the prevalence of : {patho3}',
           toolbar_location=None, tools="hover", tooltips="@prev, @annee")
p.line(x='annee', y='prev', source=source, line_width=2, line_color="#FF5733")

p.xaxis.axis_label = "Year"
p.yaxis.axis_label = "Prevalence"
st.bokeh_chart(p)

#4 Viz
st.write("So what are the most common pathologies?")
st.write('Bar graph of the top 10 level 2 pathologies')

patho_niv2 = data.groupby('patho_niv2').size().reset_index(name='count')
top10 = patho_niv2.nlargest(10, 'count')

chart = alt.Chart(top10).mark_bar().encode(
    x=alt.X('count:Q', title='Number of patients treated'),
    y=alt.Y('patho_niv2:N', title='Level 2 pathologies subgroup', sort='-x')
).properties(
    title='Top 10 most frequent level 2 pathology subgroups'
)
st.altair_chart(chart, use_container_width=True)

#5 Viz

st.write('Now, let\'s look at prevalence by age group and pathology.')
pathology = st.selectbox('Please select a pathology', data['patho_niv1'].unique(), key='1.niv1')
data_patho1 = data[data['patho_niv1'] == pathology]
age_prev = data_patho1.groupby('cla_age_5')['prev'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(age_prev['cla_age_5'], age_prev['prev'])
ax.set_xlabel('Age range (5 years)')
ax.set_ylabel('Average prevalence')
ax.set_title(f'Average prevalence of {pathology} by age range')
plt.xticks(rotation=45)
st.pyplot(fig)

#6 Viz


# Titre de la barre latérale
st.write('Priority heat map by region')
region = st.selectbox('Select a region', data['region'].unique(), key='region')
data_region = data[data['region'] == region]

fig, ax = plt.subplots(figsize=(10, 6))
heatmap_data = data_region.pivot_table(index='region', columns='niveau_prioritaire', values='npop')
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", linewidths=0.5, ax=ax)
plt.title(f'Priority heat map for the region : {region}')
plt.xlabel('Priority Level')
plt.ylabel('Region')
st.pyplot(fig)

st.caption('Marie-Ange ACCROMBESSY')
st.caption('Hope you enjoyed my visualization ! :dizzy:')
