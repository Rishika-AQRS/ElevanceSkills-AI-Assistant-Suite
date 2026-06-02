# 🚀 Task 4: ArXiv Expert Chatbot

**RAG Chatbot** for arXiv AI papers | Elevance Skills AI/ML Internship

---

## 🛠 **Project Architecture**
| Component      | Technology                    |
|----------------|-------------------------------|
| **Retrieval**  | FAISS Vector Database         |
| **Embeddings** | `all-MiniLM-L6-v2`            |
| **LLM**        | Google Gemini (`gemini-flash-latest`) |
| **Frontend**   | Streamlit                     |
| **Data**       | 47k arXiv papers metadata     |

---

*Semantic search → Top 3 papers → AI explanation with arXiv links.*

---

## 💡 **How it Works**
1. **Query Embedding** → SentenceTransformer encodes user question
2. **FAISS Search** → Retrieves top 3 most relevant arXiv papers  
3. **Paper Display** → Expandable cards with abstracts + arXiv links
4. **RAG Generation** → Gemini explains using paper context
5. **Chat Memory** → Multi-turn conversation preserved

---

## 🚀 **Setup & Execution**
```bash
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your_key" > .env
streamlit run app.py
```

## 📝 **Internship Report Summary**
* **Skills Demonstrated:** FAISS semantic search, RAG pipeline, production Streamlit UI, quota-resilient error handling
* **Challenges Overcome:** API quota management, chat state persistence, efficient paper retrieval
* **Production Ready:** Live deployment + graceful degradation

---

**Task 4 Complete** ✅ | *Rishika Rai* | *May 2026*