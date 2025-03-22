import pandas as pd

import streamlit as st

import plotly.express as px
from streamlit import subheader

st.header('display data frame')

# df = pd.DataFrame({
#     'Name':['Cristiano', 'Vini JR', 'Bellingham'],
#     'Age': [39, 24, 21],
#     'Country': ['Portugal', 'Brazil', 'Englan

#st.write(df)

book_df = pd.read_csv('module18/bestsellers.csv')

st.title('bestselling Book Analysis')
st.write('this app analyzes the amazon top selling books from 2009 to 2022.')

st.subheader("summery Statistic")
total_books = book_df.shape[0]
unique_titles = book_df['Name'].nunique()
average_rating = book_df['User Rating'].mean()
average_price = book_df['Price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique_titles",unique_titles)
col3.metric("Average_rating",f"{average_rating:.2}")
col4.metric("Average_price",f"{average_price:.2}")

st.subheader("Data Preview")
st.write(book_df.head())

col1,col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = book_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = book_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig= px.pie(book_df, names='Genre', title='Most Liked Genre (2009 - 2022)', color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)

st.plotly_chart(fig)