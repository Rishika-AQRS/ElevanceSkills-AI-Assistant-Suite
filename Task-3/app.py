import streamlit as st
import os
from data_loader import load_xml
import re
from collections import Counter


folder_path=r"D:\Users\Rishika\Internship_1\Task-3\data\4_MPlus_Health_Topics_QA"

st.set_page_config(
    page_title="MedBot: Medical Q&A ChatBot",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 MedBot: Medical Q&A ChatBot")
st.markdown("**AI-powered medical question answering using MedQuAD dataset**")

with st.spinner("Loading medical Q&A dara...."):
    docs=load_xml(folder_path)

if not docs:
    st.error("No QA pairs loaded!")
    st.stop()

def preprocess_text(text):
    text=text.lower()
    text=re.sub(r'[^\w\s]', '', text)
    words=text.split()
    stopwords={'what', 'is', 'the', 'a', 'an', 'how', 'do', 'does', 'can', 'i', 'my', 'me', 
                 'with', 'for', 'of', 'to', 'in', 'are', 'are', 'was', 'were', 'be', 'been', 
                 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
                 'should', 'may', 'might', 'must', 'shall', 'this', 'that', 'these', 'those'}
    words=[w for w in words if w not in stopwords and len(w)>2]
    return words

def calculate_tfidf_score(query_words, doc_words, all_docs_words):
    doc_word_count=Counter(doc_words)
    tf={word:count/len(doc_words) for word, count in doc_word_count.items()}
    doc_count=len(all_docs_words)
    idf={}
    for word in query_words:
        doc_with_word=sum(1 for doc in all_docs_words if word in doc)
        idf[word]=1+(doc_count/(1+doc_with_word))

    score=sum(tf.get(word, 0)*idf.get(word, 0) for word in query_words)
    return score

def find_best_answers(query, docs, top_k=3):
    query_words=preprocess_text(query)
    processed_docs=[(doc, preprocess_text(doc)) for doc in docs]
    all_docs_words=[doc_words for _, doc_words in processed_docs]
    results=[]
    for doc, doc_words in processed_docs:
        tfidf_score=calculate_tfidf_score(query_words, doc_words, all_docs_words)
        overlap=len(set(query_words) & set(doc_words))
        overlap_score=overlap/len(query_words) if query_words else 0

        combined_score=0.6*tfidf_score+0.4*overlap_score
        results.append((doc, combined_score, overlap, tfidf_score))
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:top_k]
medical_keywords={
    "Diseases": ["diabetes", "cancer", "asthma", "arthritis", "hypertension", "obesity", 
                 "anemia", "thyroid", "migraine", "allergy", "depression", "infection",
                 "pneumonia", "bronchitis", "influenza", "flu", "Covid", "coronavirus"],
    "Symptoms": ["symptom", "pain", "fever", "headache", "nausea", "vomiting", "fatigue",
                 "cough", "sneezing", "dizziness", "weakness", "swelling", "rash", "itching"],
    "Treatments": ["medication", "treatment", "therapy", "surgery", "medicine", "drug",
                   "cure", "vaccine", "injection", "dosage", "prescription", "remedy"],
    "Body Parts": ["heart", "lung", "liver", "kidney", "stomach", "brain", "blood",
                   "bone", "muscle", "skin", "eye", "ear", "throat", "chest", "back"]
}


def detect_entities(text):
    text_lower=text.lower()
    detected={}
    for category, keywords in medical_keywords.items():
        found=[kw for kw in keywords if kw in text_lower]
        if found:
            detected[category]=found
    return detected

query=st.text_input("Ask a Medical Question:", placeholder="e.g., What are the symptoms of diabetes?")

if query:
    with st.spinner("Searching medical knowledge base...."):
        results=find_best_answers(query, docs, top_k=3)

    detected_entities=detect_entities(query)

    if detected_entities:
        st.markdown("### 🔬 Medical Entities Detected")
        cols=st.columns(len(detected_entities))
        for i, (category, entities) in enumerate(detected_entities.items()):
            with cols[i]:
                st.info(f"**{category}**: {', '.join(entities)}")

    st.markdown("### 💬 Top Recommended Answers")
    for i, (answer, score, overlap, tfidf) in enumerate(results, 1):
        with st.expander(f"🏆 Answer #{i} (Confident: {score:.2f})", expanded=(i==1)):
            st.write(answer)
            col1, col2, col3=st.columns(3)
            with col1:
                st.metric("TF-IDF Score", f"{tfidf:.3f}")
                with col2:
                    st.metric("Keyword Overlap", f"{overlap} words")
            with col3:
                confidence=min(score*10, 100)
                st.metric("Confidence", f"{confidence:.1f}%")
    if results[0][1]<0.1:
        st.warning("⚠️ Low confidence match! Try rephrasing your question with more specific medical terms.")











