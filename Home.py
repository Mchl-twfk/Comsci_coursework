import streamlit as st
import sqlite3
import pandas as pd

##link sql database to python program
con = sqlite3.connect("orders.db")
cur = con.cursor()

##write title and introductory text
st.title("Restaurant order system")
st.write("-please select which page you would like to visit-")

##create table in the database
def create_table():

    cur.execute("""
                CREATE TABLE IF NOT EXISTS orders(
                table number INTEGER,
                order TEXT,
                ready? BOOLEAN
                )
                """)

##add orders to the table
def add_order():
    cur.execute(f"""
                INSERT INTO orders""")