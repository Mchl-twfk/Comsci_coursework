import streamlit as st
import sqlite3
from Home import create_table

con = sqlite3.connect("orders.db")
cur = con.cursor()


st.title("-Orders-")

clear_button = st.button("clear table", type="primary")

if clear_button:
    st.write("are you sure?")
    yes_button = st.button("Yes")
    no_button = st.button("No")


st.table()


