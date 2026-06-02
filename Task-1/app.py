# Task-1/app.py

import streamlit as st
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
import os
import traceback

# Load .env from parent folder
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
VSTORE_DIR=os.path.join(BASE_DIR, "embeddings", "faiss")

st.set_page_config(page_title="Task 1", page_icon="📚", layout="wide")

st.title("📚 Internship Task 1: Knowledge Updatable Chatbot")
st.markdown("**A chatbot that dynamically expands its knowledge base over time**")

if not os.path.exists(VSTORE_DIR):
    st.error("❌ Knowledge base not found!")
    st.info("💡 Run: `python update_knowledge.py`")
    st.stop()

api_key=os.getenv("GOOGLE_API_KEY")
if not api_key or api_key=="your_google_api_key_here":
    st.error("❌ Add GOOGLE_API_KEY to .env in parent folder")
    st.stop()

st.success("✅ Configuration OK!")

@st.cache_resource
def get_rag_chain():
    embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    db=FAISS.load_local(
        VSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )
    retriever=db.as_retriever(search_kwargs={"k": 3})
    llm=ChatGoogleGenerativeAI(model="gemini-flash-latest", google_api_key=api_key)
    
    prompt=ChatPromptTemplate.from_template(
        "You are a helpful assistant. Use the context to answer.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
    )
    
    rag_chain=(
        {"context": retriever, "question": RunnablePassthrough()} 
        | prompt 
        | llm 
        | StrOutputParser()
    )
    
    return rag_chain

try:
    with st.spinner("Loading knowledge base..."):
        rag_chain=get_rag_chain()
    st.success("✅ Knowledge base loaded!")
except Exception as e:
    st.error(f"❌ Error: {str(e)}")
    st.code(traceback.format_exc())
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt:=st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer=rag_chain.invoke(prompt)
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {str(e)}")

with st.sidebar:
    st.header("📊 Task 1 Features")
    st.markdown("""
    ✅ FAISS vector database
    ✅ SentenceTransformer embeddings
    ✅ Google Gemini LLM
    ✅ RAG pipeline
    
    **Update Knowledge:**
    1. Add `.txt` files to `sources/`
    2. Run `python update_knowledge.py`
    3. Refresh browser
    """)