import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

st.title(" Welcome to GT Chatbot")
# Load API key securely from .env file
#load_dotenv()
#api_key = os.getenv("GOOGLE_API_KEY")
api_key = st.secrets["GOOGLE_API_KEY"]

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

genai.configure(api_key=api_key)

# Create a Gemini model instance
model = genai.GenerativeModel("gemini-2.0-flash")

# Ask a question


prompt = st.text_input("Ask a question:")
if st.button("Get Answer"):
    if prompt:
        response = model.generate_content(prompt)
        st.write(response.text)