from langdetect import detect, LangDetectException
from typing import Optional
from deep_translator import GoogleTranslator

LANGUAGES={
    "en":"English",
    "hi":"Hindi",
    "es":"Spanish",
    "fr":"French",
}


SUPPORTED_CODES=set(LANGUAGES.keys())

def detect_language(text:str)->Optional[str]:
    if not text.strip():
        return None
    try:
        code=detect(text)
        code=code.lower().strip()
        return code if code in SUPPORTED_CODES else None
    except LangDetectException:
        return None
    

def get_language_name(lang_code:str)->str:
    return LANGUAGES.get(lang_code, lang_code.upper())
    
def make_response_hint(lang_code:Optional[str])->str:
    if not lang_code or lang_code=="en":
        return "Reply in clear, polite English."
    if lang_code=="hi":
        return "Reply in Hindi."
    if lang_code=="es":
        return "Reply in Spanish."
    if lang_code=="fr":
        return "Reply in French."

def to_english(text:str)->str:
    if not text.strip():
        return text
    try:
        translated=GoogleTranslator(
            source='auto',
            target='en'
        ).translate(text)

        if translated:
            return translated
        
    except Exception as e:
        print(f"Tranlation error: {e}")

    return text


def from_english(text:str, target_lang:str)->str:
    if not text.strip() or target_lang=="en":
        return text
    
    try:
        translated=GoogleTranslator(
            source='en',
            target=target_lang
        ).translate(text)

        if translated:
            return translated
        
    except Exception as e:
        print(f"Translation error: {e}")

    return text




