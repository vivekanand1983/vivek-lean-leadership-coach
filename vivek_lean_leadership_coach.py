import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
import openai

# UI setup
st.set_page_config(page_title="Vivek Lean Leadership Coach", layout="wide")
st.title("🧠 Vivek Lean Leadership Coach")
st.markdown("Your personalized lean & six sigma AI – trained on 50+ core books and statistical texts.")

# Password Protection
password = st.text_input("Enter password to continue:", type="password")
if password != "Priyav@1983!":
    st.stop()

# Set OpenAI API key
import os
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# LlamaIndex settings
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# Load documents and build index (assumes 'books' folder present)
@st.cache_resource(show_spinner="Indexing books...")
def load_index():
    docs = SimpleDirectoryReader("books").load_data()
    return VectorStoreIndex.from_documents(docs)

index = load_index()
query_engine = index.as_query_engine()

# User question input
query = st.text_input("Ask your lean or six sigma question:")
if query:
    st.write("Generating answer from Vivek's RAG library...")
    response = query_engine.query(query)
    st.success(response.response)