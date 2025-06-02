
import streamlit as st
from openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms.openai import OpenAI as LlamaOpenAI

st.set_page_config(page_title="Vivek Lean Leadership Coach", layout="wide")
st.title("🧠 Vivek Lean Leadership Coach")
st.markdown("Your personalized lean & six sigma AI – trained on 50+ core books and statistical texts.")

# Password Protection
password = st.text_input("Enter password to continue:", type="password")
if password != "Priyav@1983!":
    st.stop()

query = st.text_input("Ask your lean or six sigma question:")
if query:
    st.write("Generating answer from Vivek's RAG library...")
    try:
        service_context = ServiceContext.from_defaults(llm=LlamaOpenAI(model="gpt-3.5-turbo"))
        index = VectorStoreIndex.from_disk("lean_index.json", service_context=service_context)
        engine = index.as_query_engine()
        response = engine.query(query)
        st.success(response.response)
    except Exception as e:
        st.error(f"Error: {e}")
