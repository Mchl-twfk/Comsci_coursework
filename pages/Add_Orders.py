import streamlit as st

st.title("-Add an Order-")

tablenum = st.number_input("Table Number", min_value=1, max_value=50)

if "orderlist" not in st.session_state:
    st.session_state.orderlist = []

order_entry = st.text_input("Enter order")
Enter = st.button("Enter") 
Clear = st.button("Clear Orders")
Send = st.button("Send Order")

##add order to table list
if Enter:
    st.session_state.orderlist.append(order_entry)
##clear orders in the table group
if Clear:
    st.session_state.orderlist = []

st.session_state