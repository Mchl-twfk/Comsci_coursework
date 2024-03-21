import streamlit as st
import sqlite3
import pandas as pd
from contextlib import closing  
import random as r

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
                    return cur.execute((SQL)).fetchall()
                else:
                    return cur.execute((SQL), (inputs)).fetchall()

##create table in the database
def create_table():
    Query("""
        CREATE TABLE IF NOT EXISTS orders (
            index_num INTEGER PRIMARY KEY,
            dish_num INTEGER,
            table_number INTEGER,
            Order_Name TEXT,
            in_progress BOOLEAN,
            ready BOOLEAN
        );
    """)

def dish_no_gen(randint, randrange):
    dishnum = ()
    for i in range(1,7):
        randnum = (r.randint(0,9))
        dishnum.append(randnum)
    print(dishnum)

create_table()


