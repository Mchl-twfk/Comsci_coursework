import streamlit as st
import sqlite3
from Home import Query


con = sqlite3.connect("orders.db")
cur = con.cursor()

##add orders to the table
def add_order(input1, input2, input3, input4):
    Query("""
            INSERT INTO orders(table_number, Order_name, in_progress, ready) VALUES
            (?, ?, ?, ?);
            """, ((input1),(input2),(input3),(input4))
            )


st.title("-Add an Order-")


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
    n=0
    for i in st.session_state.orderlist:
        list_element = st.session_state.orderlist[n]
        add_order((tablenum), (list_element), (0), (0))
        n=n+1
   
st.session_state


