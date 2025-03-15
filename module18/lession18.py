import pandas as pd

import streamlit as st

st.header('display data frame')

df = pd.DataFrame({
    'Name':['Cristiano', 'Vini JR', 'Bellingham'],
    'Age': [39, 24, 21],
    'Contry': ['Portugal', 'Brazil', 'England']
})

st.write(df)