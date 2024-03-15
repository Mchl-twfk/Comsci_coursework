import streamlit as st
import sqlite3
import pandas as pd
from contextlib import closing




##SQL Query runner
def Query(SQL, inputs=()):
    with closing(sqlite3.connect("test.db")) as con:
        with con:
            with closing(con.cursor()) as cur:
                if inputs == ():
                    return cur.execute(SQL).fetchall()
                else:
                    return cur.execute(SQL, inputs).fetchall()

##create table in the database
def create_table():
    Query("""
        CREATE TABLE IF NOT EXISTS testtable (
            testfeild1 TEXT,
            testfeild2 INTEGER,
            testfeild3 TEXT
        );
    """)

##add orders to the table
def add_order():
    Query("""
            INSERT INTO orders VALUES
            (?, ?, FALSE, FALSE);
            """)


try:
    create_table()
except Exception as e:
    st.error(e)
