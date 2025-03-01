from random import choice

import streamlit as st
from streamlit import radio


def main():
    st.title('Hello World!')

if __name__ == '__main__':
 main()

if st.button("Click me!"):
    st.write("button clicked")

st.checkbox("check me")


# if st.checkbox("check me"):
#     st.write("!!!!!")

user_input = st.text_input("enter text: shkruaj nje text")
st.write("you enterd:", user_input)

age = st.number_input("Enter you age", min_value=1, max_value=100)
st.write(f"you are {age} years old")

message = st.text_area("enter text")
st.write(f"your typed {message}")

choice = st.radio("choice one",["choice1","choice2","choice3"])
st.write(f"your choice {choice}")

if st.button("success"):
    st.success("it was  successed")