# 💬 Customer Support Chatbot (Task-5)

**Streamlit chatbot** for customer service using **Bitext Customer Support LLM Training Dataset** (27K+ conversations). Includes **sentiment analysis** for support queries.

## ✨ Features
- Semantic search on Bitext customer support dataset
- **Sentiment analysis** for incoming queries
- RAG pipeline with FAISS vector search
- Multi-model support (OpenAI/Gemini)
- Real-time customer service responses
- Clean Streamlit interface

## 🛠️ Tech Stack
Python | Streamlit | FAISS | OpenAI | Google Gemini | Pandas | Sentence Transformers


## 📊 Dataset
- **Bitext Customer Support LLM Training Dataset**
- 27K+ instruction-response pairs
- 11 categories, 27 intents
- Perfect for customer service chatbots

## 🚀 Quick Start
1. Clone repo
```bash
git clone https://github.com/yourusername/task-5-customer-support-chatbot
cd task-5-customer-support-chatbot
```

2. Install
```bash
pip install -r requirements.txt
```

3. Add API keys to `.streamlit/secrets.toml`
```toml
OPENAI_API_KEY = "sk-..."
GOOGLE_API_KEY = "your-key"
```

4. Run
```bash
streamlit run app.py
```

## 📁 Structure
Task-5/
├── app.py # Streamlit app
├── data_loader.py # Bitext dataset loader
├── faiss_index.py # Vector search
├── sentiment_analyzer.py # Sentiment detection
├── requirements.txt
├── .gitignore
└── artifacts/ # Index files (ignored)


## 🧠 How it works
1. **Load**: Bitext customer support dataset
2. **Index**: FAISS vector embeddings
3. **Query**: Customer message → sentiment → top matches
4. **Response**: Context-aware support reply

## 🔑 API Keys
- OpenAI API key (GPT-4o-mini)
- Google Gemini API key (optional)

