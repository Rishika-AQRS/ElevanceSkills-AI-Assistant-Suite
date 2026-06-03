import streamlit as st

st.set_page_config(
    page_title="AI Assistant Suite",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# HERO SECTION
# =====================================================

st.title("🤖 AI Assistant Suite")

st.markdown("""
### Integrated Multi-Domain Conversational AI Platform

**Developed by Rishika Rai**  
B.Tech Computer Science Engineering | Amity University  
AI & Software Engineering Enthusiast

This project was developed as part of an AI Internship Program and integrates six intelligent chatbot systems into a single unified platform.

The suite demonstrates practical applications of:

- Generative AI
- Retrieval-Augmented Generation (RAG)
- Vector Search
- Sentiment Analysis
- Multilingual AI
- Multi-Modal AI
- Research Paper Retrieval
- Medical Question Answering
""")

st.markdown("---")

# =====================================================
# PROJECT OVERVIEW
# =====================================================

st.header("📊 Project Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("AI Modules", "6")

with col2:
    st.metric("Languages", "4")

with col3:
    st.metric("Datasets", "3+")

with col4:
    st.metric("Core Technologies", "10+")

st.markdown("---")

# =====================================================
# MODULES
# =====================================================

st.header("🚀 Integrated AI Modules")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 📚 Knowledge Base Chatbot

Dynamic Retrieval-Augmented Generation (RAG) chatbot capable of expanding its knowledge base automatically through scheduled updates and vector database refresh mechanisms.
""")

    st.info("""
### 🩺 Medical Q&A Chatbot

Specialized healthcare assistant developed using the MedQuAD dataset with medical entity recognition and intelligent answer retrieval.
""")

    st.info("""
### 💬 Sentiment-Aware Support Chatbot

Customer support assistant capable of detecting user emotions and adapting responses based on sentiment intensity.
""")

with col2:

    st.info("""
### 🖼️ Multi-Modal Assistant

Gemini-powered chatbot capable of understanding image uploads and generating contextual responses using visual and textual information.
""")

    st.info("""
### 🔬 Research Expert Assistant

Scientific research companion trained on arXiv papers with paper retrieval, concept explanation, and research summarization capabilities.
""")

    st.info("""
### 🌍 Multilingual Support Chatbot

Supports English, Hindi, French, and Spanish with automatic language detection and multilingual response generation.
""")

st.markdown("---")

# =====================================================
# INTERNSHIP OBJECTIVES
# =====================================================

st.header("✅ Internship Objectives Achieved")

st.success("""
✔ Dynamic Knowledge Base Expansion

✔ Multi-Modal AI Interaction

✔ Medical Question Answering System

✔ Research Paper Retrieval & Summarization

✔ Sentiment-Aware Customer Support

✔ Multilingual Conversational AI
""")

st.markdown("---")

# =====================================================
# SYSTEM ARCHITECTURE
# =====================================================

st.header("🏗️ System Architecture")

st.code(
"""
┌──────────────────────────────┐
│            User              │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Streamlit Frontend      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      AI Assistant Suite      │
├──────────────────────────────┤
│ Task 1 - Knowledge Chatbot   │
│ Task 2 - Multi-Modal AI      │
│ Task 3 - Medical Q&A         │
│ Task 4 - Research Expert     │
│ Task 5 - Sentiment Support   │
│ Task 6 - Multilingual AI     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      AI Processing Layer     │
├──────────────────────────────┤
│ Google Gemini 1.5 Flash      │
│ Sentence Transformers        │
│ FAISS Vector Search          │
│ Translation Engine           │
│ Sentiment Analysis Engine    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Data Sources         │
├──────────────────────────────┤
│ MedQuAD Dataset              │
│ arXiv Research Dataset       │
│ Support Knowledge Base       │
│ Custom Knowledge Sources     │
└──────────────────────────────┘
"""
)

st.markdown("---")

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.header("🛠️ Technology Stack")

frontend, ai, data = st.columns(3)

with frontend:
    st.markdown("""
### Frontend

- Streamlit
- Python
- Interactive UI Components
""")

with ai:
    st.markdown("""
### AI & NLP

- Google Gemini Flash
- LangChain
- Sentence Transformers
- HuggingFace
- NLTK
- Generative AI
""")

with data:
    st.markdown("""
### Data & Retrieval

- FAISS
- Pandas
- NumPy
- MedQuAD Dataset
- arXiv Dataset
- Custom Knowledge Sources
""")

st.markdown("---")

# =====================================================
# ABOUT THE DEVELOPER
# =====================================================

st.header("👩‍💻 About the Developer")

st.markdown("""
### Rishika Rai

**B.Tech Computer Science Engineering**  
**Amity University**

Currently pursuing undergraduate studies in Computer Science Engineering with a strong interest in:

- Artificial Intelligence
- Machine Learning
- Generative AI
- Retrieval-Augmented Generation (RAG)
- Natural Language Processing
- Software Development

This project represents the successful integration of six independent AI applications into a unified conversational platform capable of handling multiple real-world use cases.
""")

st.markdown("---")

# =====================================================
# NAVIGATION
# =====================================================

st.header("📂 Explore the Platform")

st.info(
    "Use the sidebar to access all six AI modules and explore their capabilities."
)

st.markdown("---")

st.caption(
    "AI Assistant Suite | Developed by Rishika Rai | AI Internship Project 2026"
)