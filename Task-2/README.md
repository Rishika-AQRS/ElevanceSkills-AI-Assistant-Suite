# 🚀 Task 2: Multimodal Chatbot

This project extends the RAG chatbot to handle multimodal inputs, allowing users to upload images for analysis alongside text queries.

## 🛠 Tech Stack
* **Language:** Python
* **Vision Model:** Gemini (`gemini-flash-latest`)
* **UI:** Streamlit

## 📸 Functionality
* **Image Analysis:** Uses `Pillow` to process uploads before sending them to Gemini.
* **Unified Prompting:** Merges image data and text into a single context for the LLM.

## 🚀 Setup
1. `pip install -r requirements.txt`
2. `streamlit run app.py`