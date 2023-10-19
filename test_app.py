import streamlit as st

tabs = st.tabs(["Tab 1", "Tab 2"])

with tabs[0]:
    st.header("This is tab 1")

with tabs[1]:
    st.header("This is tab 2")
