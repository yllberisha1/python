import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
book_df = pd.read_csv('module18/bestsellers.csv')

# Display header and title
st.title('Bestselling Book Analysis')
st.write('This app analyzes the Amazon top-selling books from 2009 to 2022.')

st.sidebar.header("Add New Book Data")

# Create the form in the sidebar
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("User Rating", 0.5, 5.0, 0.0, 0.1)
    new_review = st.number_input('Review', min_value=0, step=1)
    new_price = st.number_input('Price', min_value=0, step=1)
    new_year = st.number_input('Year', min_value=2009, max_value=2022, step=1)
    new_Genre = st.selectbox("Genre", book_df['Genre'].unique())
    submit_button = st.from_submit_button(label="Add Book")




# Summary statistics section
st.subheader("Summary Statistics")
total_books = book_df.shape[0]
unique_titles = book_df['Name'].nunique()
average_rating = book_df['User Rating'].mean()
average_price = book_df['Price'].mean()

# Display the metrics in columns
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")

# Data Preview section
st.subheader("Data Preview")
st.write(book_df.head())

# Top 10 Book Titles Visualization
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = book_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors = book_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

# Genre Distribution Pie Chart
st.subheader("Genre Distribution")
fig = px.pie(book_df, names='Genre', title='Most Liked Genre (2009 - 2022)', color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

# Top 15 Authors by Count of Books Published
st.header('Top 15 Authors by Count of Books Published')
top_authors = book_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']

size = book_df.groupby(['Year', 'Genre']).size().reset_index(name='Counts')

fig = px.bar(size,
             x='Year',
             y='Counts',
             title='Number of Fiction vs Non-Fiction Books from 2009-2022',
             color='Genre',
             color_discrete_sequence=px.colors.sequential.Plasma,
             barmode='group')

st.subheader("Number of Fiction vs Non-Fiction Books Over the Years")
st.plotly_chart(fig)


fig = px.bar(top_authors, x='Count', y='Author', orientation='h',
             title='Top 15 Authors by Counts of Books Published',
             labels={'Count': "Counts of Books Published", 'Author': 'Author'},
             color='Count', color_continuous_scale=px.colors.sequential.Plasma)

st.plotly_chart(fig)

st.subheader("Filter Data by Genre")


genre_filter = st.selectbox('Select Genre', book_df['Genre'].unique())


filter_df = book_df[book_df['Genre'] == genre_filter]


if filter_df.empty:
    st.write(f"No data available for the genre: {genre_filter}")
else:
    #
    st.write(filter_df)
