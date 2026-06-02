def count_sentiments(logs, limit=5):
    recent=logs[-limit:]
    counts={
        "positive":0,
        "neutral":0,
        "negative":0,
        "strong_positive":0,
        "strong_negative":0
    }

    for item in recent:
        sentiment=item.get("sentiment")
        intensity=item.get("intensity")
        if sentiment in counts:
            counts[sentiment]+=1
        if intensity in counts:
            counts[intensity]+=1
    return counts

def get_dominant_sentiment(logs, limit=5):
    counts=count_sentiments(logs, limit)
    dominant_sentiment=max(counts, key=counts.get)
    return dominant_sentiment, counts

