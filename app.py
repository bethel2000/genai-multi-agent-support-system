import streamlit as st
from agents.router import route_query

st.title("GenAI Multi-Agent Customer Support System")

query = st.text_input("Ask a question:")

if query:
    response = route_query(query)
    st.write("### Response:")
    st.write(response)
