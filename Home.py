import streamlit as st
import sqlite3


con = sqlite3.connect("orders.db")
cur = con.cursor()

st.title("Resturant order system")

st.write("-please select which page you would like to visit-")

def create_table():
    cur.execute("""
                CREATE TABLE IF NOT EXISTS orders(
                table number INTEGER,
                order TEXT,
                ready? BOOLEAN
                )
                """)