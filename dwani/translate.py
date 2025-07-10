from .exceptions import DwaniAPIError
import requests

# Language options mapping
language_options = [
    ("English", "eng_Latn"),
    ("Kannada", "kan_Knda"),
    ("Hindi", "hin_Deva"), 
    ("Assamese", "asm_Beng"),
    ("Bengali", "ben_Beng"),
    ("Gujarati", "guj_Gujr"),
    ("Malayalam", "mal_Mlym"),
    ("Marathi", "mar_Deva"),
    ("Odia", "ory_Orya"),
    ("Punjabi", "pan_Guru"),
    ("Tamil", "tam_Taml"),
    ("Telugu", "tel_Telu"),
    ("German", "deu_Latn") 
]

# Create dictionaries for language name to code and code to code mapping
lang_name_to_code = {name.lower(): code for name, code in language_options}
lang_code_to_code = {code: code for _, code in language_options}

def normalize_language(lang):
    """Convert language input (name or code) to language code."""
    lang = lang.strip()
    lang_lower = lang.lower()
    if lang_lower in lang_name_to_code:
        return lang_name_to_code[lang_lower]
    if lang in lang_code_to_code:
        return lang_code_to_code[lang]
    supported_langs = list(lang_name_to_code.keys()) + list(lang_code_to_code.keys())
    raise ValueError(f"Unsupported language: {lang}. Supported languages: {supported_langs}")

def split_into_sentences(text):
    """Split a string into sentences based on full stops."""
    if not text.strip():
        return []
    # Split on full stops, preserving non-empty sentences
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    return sentences

def run_translate(client, sentences, src_lang, tgt_lang):
    """Translate sentences in a single API call."""
    # Convert single string to list of sentences if necessary
    if isinstance(sentences, str):
        sentences = split_into_sentences(sentences)
    elif not isinstance(sentences, list):
        raise ValueError("sentences must be a string or a list of strings")
    
    # Validate that all elements in the list are strings
    if not all(isinstance(s, str) for s in sentences):
        raise ValueError("All sentences must be strings")
    
    # Normalize source and target languages
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/translate"
    payload = {
        "sentences": sentences,
        "src_lang": src_lang_code,
        "tgt_lang": tgt_lang_code
    }
    resp = requests.post(
        url,
        headers={**client._headers(), "Content-Type": "application/json", "accept": "application/json"},
        json=payload,
        timeout=90
    )
    if resp.status_code != 200:
        raise DwaniAPIError(resp)
    return resp.json()

class Translate:
    @staticmethod
    def run_translate(sentences, src_lang, tgt_lang):
        from . import _get_client
        return run_translate(_get_client(), sentences, src_lang, tgt_lang)