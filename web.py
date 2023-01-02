import streamlit as st
import functions

todos = functions.get_todos()

st.title("My ToDo App")

st.subheader("This is my ToDo Web App.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add New ToDo...")