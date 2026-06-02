import google.generativeai as genai
import streamlit as st
import pandas as pd
import os
from sentence_transformers import SentenceTransformer
import faiss
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model=genai.GenerativeModel('gemini-flash-latest')

st.set_page_config(page_title="ArXiv Expert ChatBot", layout="wide")
st.title("ArXiv Expert: AI Research Assistant")

@st.cache_resource
def load_resources():
    metadata=pd.read_pickle('Task-4/data/vector_db/papers_metadata.pk1')
    index=faiss.read_index('Task-4/data/vector_db/arxv_papers.index')
    embedding_model=SentenceTransformer('all-MiniLM-L6-v2')
    return metadata, index, embedding_model

metadata, index, embedding_model=load_resources()

if "messages" not in st.session_state:
    st.session_state.messages=[]
if "last_paper_title" not in st.session_state:
    st.session_state.last_paper_title=""
if "last_paper_abstract" not in st.session_state:
    st.session_state.last_paper_abstract=""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:=st.chat_input("Ask a question about AI research!"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        history_text="\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
        
        v=embedding_model.encode([prompt]).astype('float32')
        distance, indices=index.search(v, k=3)

        retrieved_data=[]
        
        for i in indices[0]:
            paper=metadata.iloc[i]
            retrieved_data.append(f"Title: {paper['title']}\\nAbstracts: {paper['abstract']}")
            
            with st.expander(f"{paper['title']}"):
                st.write(f"**Abstract:** {paper['abstract']}")
                st.write(f"[Link to arXiv] (https://arxiv.org/abs/{paper['id']})")
                
        context="\n\n".join(retrieved_data)
        history_text="\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[:-1]])
        full_prompt=f"""
        You are an expert scientific assistant,
        Conversation History: {history_text}
        Use the following research abstracts to explain the answer.
        Research Context: {context}
        Question: {prompt}

        """
        with st.spinner("Generating AI Explanation...."):
            try:
                model=genai.GenerativeModel('gemini-flash-latest')
                response=model.generate_content(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content":response.text})
            except Exception as e:
                st.warning("AI explanation is temporarily unavailable due to API limits. Showing retrieved papers only!")
                st.write("Try again in a few seconds.")
                st.caption(str(e))


