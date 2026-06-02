# Multilingual reply templates
REPLY_TEMPLATES = {
    "en": {
        "fallback": "I couldn't find a strong match. Please rephrase your question with a few more details.",
        "negative_low_score": "I'm sorry this is frustrating. I found the closest support answer I could. {answer}",
        "positive": "Glad that helped! {answer}",
    },
    "hi": {
        "fallback": "मैं आपका सवाल सही से समझ नहीं पा रहा। कृपया थोड़ा और विवरण दें।",
        "negative_low_score": "माफ़ कीजिए, यह बहुत परेशान करने वाला है। मैंने जो सबसे अच्छा उत्तर पाया, वह यह है: {answer}",
        "positive": "खुश हूँ कि यह मदद कर पाया: {answer}",
    },
    "fr": {
        "fallback": "Je n'ai pas trouvé de réponse claire. Veuillez reformuler votre question avec plus de détails.",
        "negative_low_score": "Je suis désolé que cela soit frustrant. Voici la réponse la plus proche que j'ai trouvée : {answer}",
        "positive": "Content que cela ait aidé : {answer}",
    },
    "es": {
        "fallback": "No encontré una respuesta clara. Por favor, reformule su pregunta con más detalles.",
        "negative_low_score": "Lamento que esto sea frustrante. Esta es la respuesta más cercana que encontré: {answer}",
        "positive": "Me alegra que esto haya ayudado: {answer}",
    },
}







def build_response(sentiment, results, lang_hint="Reply in clear, polite English.", lang_code="en"):
    label=sentiment["label"]
    intensity=sentiment["intensity"]
    templates=REPLY_TEMPLATES.get(lang_code, REPLY_TEMPLATES["en"])

    

    if not results:
        if label=="negative":
            return templates["fallback"]
        return templates["fallback"]

    best=results[0]
    answer=best.get("response", "")
    score=best.get("score", 0)

    if label=="negative":
        prefix="I am sorry this is frustrating. "
        if intensity=="strong_negative":
            prefix+="I understand this is important. "
        return prefix + answer
    if label=="positive":
        return "Glad that helped! " + answer
    if score < 0.35:
        return "I found the closest support answer I could. " + answer
    return answer