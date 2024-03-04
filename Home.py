import streamlit as st
import sqlite3
import pandas as pd
from contextlib import closing  


##link sql database to python program
con = sqlite3.connect("orders.db")
cur = con.cursor()

##write title and introductory text
st.title("Restaurant order system")
st.write("-please select which page you would like to visit-")

##SQL Query runner
def Query(SQL, inputs=()):
    with closing(sqlite3.connect("orders.db")) as con:
        with con:
            with closing(con.cursor()) as cur:
                if inputs == ():
                    Records = cur.execute(SQL)
                    return Records.fetchall()
                else:
                    cur.execute(SQL, inputs)

##create table in the database
def create_table():

    Query("""CREATE TABLE IF NOT EXISTS orders(
            table number INTEGER,
            order TEXT,
            in progress BOOLEAN,
            ready? BOOLEAN
            )
            """)
    con.commit()

##add orders to the table
def add_order():
    cur.execute(f"""
                INSERT INTO orders
                st.session_state.orderlist""")




