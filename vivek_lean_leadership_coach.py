
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import CondenseQuestionChatEngine
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.extractors import TitleExtractor, KeywordExtractor, QuestionsAnsweredExtractor, SummaryExtractor
from llama_index.core import Settings
from qdrant_client import QdrantClient
import os

# Streamlit App Config
st.set_page_config(page_title="Vivek Lean Leadership Coach", layout="wide")
st.title("🧠 Vivek Lean Leadership Coach")
st.markdown("Your personalized lean & six sigma AI – trained on 50+ core books and statistical texts.")

# Password Protection
password = st.text_input("Enter password to continue:", type="password")
if password != "Priyav@1983!":
    st.stop()

# Load environment variables
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Updated llama_index Settings
Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.2)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)

# Load chat engine from Qdrant vector store
client = QdrantClient(":memory:")
store = QdrantVectorStore(client=client, collection_name="vivek-lean-leadership")
index = VectorStoreIndex.from_vector_store(store)

memory = ChatMemoryBuffer.from_defaults(token_limit=3900)
chat_engine = CondenseQuestionChatEngine.from_defaults(
    retriever=index.as_retriever(similarity_top_k=5),
    memory=memory,
)

# Ask user query
query = st.text_input("Ask your lean or six sigma question:")
if query:
    st.write("Generating answer from Vivek's RAG library...")
    response = chat_engine.chat(query)
    st.success(response.response)
