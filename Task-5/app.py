import streamlit as st
from retrieval_engine import RetrievalEngine
from sentiment_analysis import get_sentiment
from response_engine import build_response

st.set_page_config(page_title="Support Chatbot", page_icon="💬", layout="centered")
st.title("💬 Sentiment-Aware Support Chatbot")
st.caption("Retrieval-based customer support chatbot with sentiment-aware responses.")

if "messages" not in st.session_state:
    st.session_state.messages=[
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

if "logs" not in st.session_state:
    st.session_state.logs=[]

if "retrieval" not in st.session_state:
    st.session_state.retrieval = RetrievalEngine("artifacts")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt=st.chat_input("Ask a support question...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    sentiment=get_sentiment(prompt)
    results=st.session_state.retrieval.search(prompt, top_k=3)
    reply=build_response(sentiment, results)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.session_state.logs.append({
    "message": prompt,
    "sentiment": sentiment["label"],
    "intensity": sentiment["intensity"],
    "compound": round(sentiment["compound"], 4),
    "top_match": results[0].get("instruction", "") if results else "",
    "top_score": round(results[0].get("score", 0), 4) if results else 0,
    "response": reply
})

    st.rerun()

with st.expander("Debug / Matches"):
    for item in reversed(st.session_state.logs[-8:]):
        st.markdown(f"**User:** {item['message']}")
        st.markdown(f"**Sentiment:** `{item['sentiment']}` | **Intensity:** `{item['intensity']}` | **Compound:** `{item['compound']}`")
        st.markdown(f"**Top match:** {item['top_match']} (`{item['top_score']}`)")
        st.markdown(f"**Bot:** {item['response']}")
        st.markdown("---")