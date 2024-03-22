import streamlit as st
import sqlite3
import pandas as pd
from Home import create_table

con = sqlite3.connect("orders.db")
cur = con.cursor()


st.title("-Orders-")

create_table()

##make the table visible on the page
orderdata = pd.read_sql_query("SELECT * FROM orders ORDER BY index_num DESC;", con)
df = pd.DataFrame(orderdata)
st.table(df)




