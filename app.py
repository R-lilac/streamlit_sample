import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.title('My page')

st.write("Good morning")

st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.markdown('# Markdown documents')


animals = ['giraffes', 'orangutans', 'monkeys']
populations = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=animals, y=populations)])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "Animal",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='Title')

st.plotly_chart(fig, use_container_width=True)