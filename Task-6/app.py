import streamlit as st
from retrieval_engine import RetrievalEngine
from sentiment_analysis import get_sentiment
from response_engine import build_response
from language_util import detect_language, get_language_name, make_response_hint, to_english, from_english

st.set_page_config(page_title="Support Chatbot", page_icon="💬", layout="centered")
st.title("💬 Multilingual Sentiment-Aware Support Chatbot")
st.caption("Retrieval-based customer support chatbot with sentiment-aware responses in 4 different languages (Hindi, English, Spanish and French).")



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
    user_lang = detect_language(prompt)
    lang_name = get_language_name(user_lang) if user_lang else "Unknown"
    lang_hint = make_response_hint(user_lang)

    st.session_state.messages.append({"role": "user", "content": prompt})

    # 1. Translate to English for search
    input_for_search = to_english(prompt) if user_lang != "en" else prompt

    if user_lang:
        locale_hint={
            "hi":"in Hindi",
            "fr":"in French", 
            "es":"in Spanish"
        }.get(user_lang, "")

        input_for_search=(
            f"{locale_hint} {input_for_search} customer support query"
        ).strip()

    # 2. Sentiment + retrieval
    sentiment = get_sentiment(input_for_search)
    results = st.session_state.retrieval.search(input_for_search, top_k=3)
    english_reply = build_response(sentiment, results, lang_hint=lang_hint)

    # 3. Translate reply back to user language (if not English)
    if user_lang and user_lang != "en":
        reply = from_english(english_reply, user_lang)
    else:
        reply = english_reply

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
    st.caption(f"Detected Language: **{lang_name}**")


    if user_lang and user_lang!="en":
        try:
            reply=from_english(english_reply, user_lang)
        except Exception:
            reply=(
                f"Sorry, I couldn't translate this. Original reply:\n\n{english_reply}"
            )

    else:
        english_reply


    st.session_state.logs.append({
        "message": input_for_search,
        "sentiment": sentiment["label"],
        "intensity": sentiment["intensity"],
        "compound": round(sentiment["compound"], 4),
        "top_match": results[0].get("instruction", "") if results else "",
        "top_score": round(results[0].get("score", 0), 4) if results else 0,
        "response": english_reply,
        "user_lang": lang_name,
    })

    st.rerun()