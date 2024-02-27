import streamlit as st

st.title("-Add an Order-")

tablenum = st.number_input("Table Number", min_value=1, max_value=50)

if "orderlist" not in st.session_state:
    st.session_state.orderlist = []

order_entry = st.text_input("Enter order")
Enter = st.button("Enter")
if Enter:
    st.session_state.orderlist.append(order_entry)

st.session_state