import streamlit as st
from streamlit import header

# col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
#
# with col1:
#      st.header('Colum1')
#      st.write('comment for colum 1')
# with col1:
#      st.header('Colum2')
#      st.write('comment for colum 2')
# with col1:
#      st.header('Colum3')
#      st.write('comment for colum 3')
# with col1:
#      st.header('colum4')
#      st.write('comment for colum 4')
# with col1:
#      st.header('colum5')
#      st.write('comment for colum 5')
#

with st.form("my_form",clear_on_submit=True):
    name = st.text_input("Name")
    age = st.slider("Age", min_value=0, max_value=100)
    email = st.text_input("Email")
    biography = st.text_area("short bio")
    terms = st.checkbox('I agree to the terms')
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Email: {email}")
    st.write(f"short bio: {biography}")

    if terms:
        st.write('your agreed to the terms')
    else:
        st.write("your cannot continue")




tab1, tab2, tab3, = st.tabs(["tab1", "tab2", "tab3"])

with tab1:
    st.header("tab1")
    st.write("tab1 desc")
with tab2:
    st.header("tab2")
    st.write("tab2 desc")
with tab3:
    st.header("tab3")
    st.write("tab3 desc")


