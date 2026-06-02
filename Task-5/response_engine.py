def build_response(sentiment, results):
    label=sentiment["label"]
    intensity=sentiment["intensity"]

    if not results:
        if label=="negative":
            return "I am sorry you're facing this issue. Please give me a few more details so I can help better."
        return "I couldn't find a strong match. Please rephrase your question with a few more details."
    best=results[0]
    answer=best.get("response", "")
    score=best.get("score", 0)

    if label=="negative":
        prefix="I am sorry this is frustrating. "
        if intensity=="strong_negative":
            prefix+="I understand this is important. "
        return prefix+answer
    if label=="positive":
        return "Glad that helped !"+answer
    if score<0.35:
        return "I found the closest support answer I could. "+answer
    return answer
