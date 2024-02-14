import streamlit as st

st.title("-Add an Order-")

tablenum = st.number_input("Table Number", min_value=1, max_value=50)

order = st.text_input("Order")


