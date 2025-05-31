
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Vivek Lean Leadership Coach", layout="wide")
st.title("🧠 Vivek Lean Leadership Coach")
st.markdown("Your personalized lean & six sigma AI – trained on 50+ core books and statistical texts.")

# Password Protection
password = st.text_input("Enter password to continue:", type="password")
if password != "Priyav@1983!":
    st.stop()

# Ask user for input
query = st.text_input("Ask your lean or six sigma question:")
if query:
    st.write("Generating answer from Vivek's RAG library...")
    # Simulated answer placeholder
    st.success("This is a placeholder answer based on your lean & six sigma library.")
