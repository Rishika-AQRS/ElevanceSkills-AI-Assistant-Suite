# 🤖 AI Assistant Suite

A comprehensive multi-feature AI platform developed as part of the ElevanceSkills AI Internship Program. This application integrates multiple specialized AI assistants into a single Streamlit-based interface, demonstrating Retrieval-Augmented Generation (RAG), Natural Language Processing (NLP), Multilingual AI, Sentiment Analysis, Medical Question Answering, and Multi-Modal AI capabilities.

---

## 🚀 Project Overview

The AI Assistant Suite combines six intelligent chatbot systems into a unified platform. Each module is designed to solve a specific real-world problem while showcasing modern AI technologies such as LangChain, FAISS, Google Gemini, Sentence Transformers, and Streamlit.

The platform provides users with:

* Dynamic knowledge retrieval and updating
* Medical question answering
* Scientific research assistance
* Multi-modal text and image interactions
* Sentiment-aware conversations
* Multilingual communication support

---

## ✨ Features

### 📚 Dynamic Knowledge Base Chatbot

A Retrieval-Augmented Generation (RAG) chatbot capable of continuously expanding its knowledge base.

**Features**

* FAISS Vector Database
* Semantic Search
* Automated Knowledge Updates
* Document Ingestion Pipeline
* Scheduled Knowledge Refresh

**Outcome**

* Automatically incorporates newly added information into future responses.

---

### 🖼️ Multi-Modal Chatbot

An AI assistant capable of processing and generating both textual and visual content.

**Features**

* Image Understanding
* Image-Based Question Answering
* Text Generation
* Visual and Textual Context Integration
* Gemini AI Integration

**Outcome**

* Enables seamless conversations involving both images and text.

---

### 🏥 Medical Q&A Assistant

A specialized healthcare information chatbot built using the MedQuAD dataset.

**Features**

* Medical Question Answering
* Disease Recognition
* Symptom Identification
* Treatment Information Retrieval
* Streamlit-Based User Interface

**Dataset**

* MedQuAD Dataset

**Outcome**

* Provides accurate retrieval-based answers to medical questions.

---

### 🔬 Research Paper Expert Assistant

A domain-specific chatbot trained on scientific literature from the arXiv dataset.

**Features**

* Research Paper Search
* Scientific Concept Explanation
* Research Summarization
* Information Extraction
* Follow-Up Question Handling

**Dataset**

* arXiv Research Papers (Computer Science Subset)

**Outcome**

* Explains complex scientific concepts and summarizes academic research.

---

### 😊 Sentiment-Aware Chatbot

A conversational assistant that adapts responses according to user emotions.

**Features**

* Sentiment Detection
* Positive Sentiment Recognition
* Negative Sentiment Recognition
* Neutral Sentiment Recognition
* Adaptive Response Generation

**Outcome**

* Improves conversational quality through emotionally aware interactions.

---

### 🌍 Multilingual AI Assistant

A chatbot supporting multiple languages with automatic language detection.

**Features**

* Automatic Language Detection
* Multi-Language Support
* Context Preservation Across Languages
* Enhanced Language Understanding
* Cultural Adaptation

**Supported Languages**

* English
* Hindi
* Spanish
* Additional Languages Supported

**Outcome**

* Enables seamless multilingual conversations without manual language switching.

---

## 🛠️ Technology Stack

### AI & NLP

* Google Gemini
* LangChain
* Sentence Transformers
* Hugging Face Models

### Retrieval & Search

* FAISS Vector Database
* Semantic Search
* Retrieval-Augmented Generation (RAG)

### Development

* Python
* Streamlit

### Data Processing

* Pandas
* NumPy

### Scheduling & Automation

* Schedule
* Watchdog

---

## 📁 Project Structure

```text
AI-Assistant-Suite/
│
├── app.py
├── pages/
│   ├── Dynamic_Knowledge_Chatbot.py
│   ├── Medical_QA_Assistant.py
│   ├── Research_Expert.py
│   ├── Multimodal_Assistant.py
│   ├── Sentiment_Assistant.py
│   └── Multilingual_Assistant.py
│
├── Task-1/
├── Task-2/
├── Task-3/
├── Task-4/
├── Task-5/
└── Task-6/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd AI-Assistant-Suite

python -m venv venv

source venv/bin/activate
# Windows:
# .\venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🎯 Internship Objectives Achieved

✅ Dynamic Knowledge Base Expansion

✅ Multi-Modal Chatbot Development

✅ Medical Question Answering System

✅ Scientific Research Expert Assistant

✅ Sentiment-Aware Conversational AI

✅ Multilingual Chatbot Support

---

## 👩‍💻 Author

**Rishika Rai**

Developed as part of the ElevanceSkills AI Internship Program.
