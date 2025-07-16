import streamlit as st

st.title("Demo App")

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.write(f"Hello welcome to Stremlit, {name} 👋")
