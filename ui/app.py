import streamlit as st
import requests

st.title("Learning Assistant")

# Input field for user query
query = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if query:
        response = requests.get(f"http://127.0.0.1:8000/ask/?query={query}")
        if response.status_code == 200:
            st.write("**Answer:**")
            st.write(response.json()["answer"])
        else:
            st.error("Server Error. Try Again!")