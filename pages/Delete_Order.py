import streamlit as st
from Home import Query

st.title("Remove an order")

def clear_table():
    Query("DROP TABLE orders;")

deletenum = st.number_input("Enter the index number of the order you would like to remove")
delete = st.button("delete")
if delete:
    Query(f"""DELETE FROM orders WHERE index_num = {deletenum}""")

clear_button = st.button("Clear table")

##clear the whole table
if clear_button:
    st.write("are you sure?")
    yes_button = st.button("Yes", type = "secondary", on_click=clear_table,)
    no_button = st.button("No")

