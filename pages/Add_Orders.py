import streamlit as st
from Home import add_order
import sqlite3

st.title("-Add an Order-")

con = sqlite3.connect("orders.db")
cur = con.cursor()


tablenum = st.number_input("Table Number", min_value=1, max_value=50)
tablenum
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

##sends the order to the database
if Send:
    try:
        for i in st.session_state.orderlist:
            add_order()
    except Exception as e:
        e

st.session_state