import streamlit as st
import sqlite3
import pandas as pd
from Home import create_table, add_order, Query

con = sqlite3.connect("orders.db")
cur = con.cursor()


st.title("-Orders-")

clear_button = st.button("clear table", type="primary")

##clear the whole table
if clear_button:
    st.write("are you sure?")
    yes_button = st.button("Yes")
    no_button = st.button("No")
    if yes_button:
        Query("DELETE * FROM orders;")

orderdata = pd.read_sql_query("SELECT * FROM orders;", con)
df = pd.DataFrame(orderdata)
st.table(df)




