import streamlit as st
import sqlite3
import pandas as pd
from Home import Query

con = sqlite3.connect("orders.db")
cur = con.cursor()


st.title("-Orders-")

clear_button = st.button("clear table", type="primary")

##clear the whole table
if clear_button:
    st.write("are you sure?")
    yes_button = st.button("Yes", type = "secondary")
    no_button = st.button("No")
    if yes_button:
        Query("DELETE * FROM orders;")


##make the table visible on the page
orderdata = pd.read_sql_query("SELECT * FROM orders ORDER BY index_num DESC;", con)
df = pd.DataFrame(orderdata)
st.table(df)




