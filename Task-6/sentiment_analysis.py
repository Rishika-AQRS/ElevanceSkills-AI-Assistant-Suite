import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()

NEGATIVE_OVERRIDE_PHRASES = [
    "dont understand", "do not understand", "not working", "frustrating",
    "frustrated", "angry", "upset", "annoying", "confusing", "problem", "issue", "error"
]

POSITIVE_OVERRIDE_PHRASES = [
    "thank you", "thanks", "great", "awesome", "perfect", "good job", "nice", "love it"
]

def normalize_text(text):
    text=text.lower().strip()
    text=re.sub(r"\bu\b", "you", text)
    text=re.sub(r"\bdont\b", "don't", text)
    text=re.sub(r"\bcant\b", "can't", text)
    text=re.sub(r"\bwont\b", "won't", text)
    text=re.sub(r"\bim\b", "i'm", text)
    return text

def get_sentiment(text):
    normalized=normalize_text(text)

    for phrase in NEGATIVE_OVERRIDE_PHRASES:
        if phrase in normalized:
            return {"label": "negative", "intensity": "negative", "compound": -0.8}

    for phrase in POSITIVE_OVERRIDE_PHRASES:
        if phrase in normalized:
            return {"label": "positive", "intensity": "positive", "compound": 0.8}

    scores=analyzer.polarity_scores(normalized)
    compound=scores["compound"]

    if compound>=0.05:
        label="positive"
    elif compound<=-0.05:
        label="negative"
    else:
        label="neutral"

    if compound<=-0.75:
        intensity="strong_negative"
    elif compound<=-0.05:
        intensity="negative"
    elif compound>=0.75:
        intensity="strong_positive"
    elif compound>=0.05:
        intensity="positive"
    else:
        intensity="neutral"

    return {"label": label, "intensity": intensity, "compound": compound}