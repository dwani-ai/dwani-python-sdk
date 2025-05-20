from .exceptions import DhwaniAPIError
import requests

# Language options mapping
language_options = [
    ("English", "eng_Latn"),
    ("Kannada", "kan_Knda"),
    ("Hindi", "hin_Deva"), 
    ("Assamese", "asm_Beng"),
    ("Bengali","ben_Beng"),
    ("Gujarati","guj_Gujr"),
    ("Malayalam","mal_Mlym"),
    ("Marathi","mar_Deva"),
    ("Odia","ory_Orya"),
    ("Punjabi","pan_Guru"),
    ("Tamil","tam_Taml"),
    ("Telugu","tel_Telu") 
]

# Create a dictionary for language name to code mapping
lang_name_to_code = {name.lower(): code for name, code in language_options}
lang_code_to_code = {code: code for _, code in language_options}

def normalize_language(lang):
    """Convert language input (name or code) to language code."""
    lang = lang.strip()
    # Check if input is a language name (case-insensitive)
    lang_lower = lang.lower()
    if lang_lower in lang_name_to_code:
        return lang_name_to_code[lang_lower]
    # Check if input is a language code
    if lang in lang_code_to_code:
        return lang_code_to_code[lang]
    # Raise error if language is not supported
    supported_langs = list(lang_name_to_code.keys()) + list(lang_code_to_code.keys())
    raise ValueError(f"Unsupported language: {lang}. Supported languages: {supported_langs}")

def chat_create(client, prompt, src_lang, tgt_lang, **kwargs):
    # Normalize source and target languages
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/indic_chat"
    payload = {
        "prompt": prompt,
        "src_lang": src_lang_code,
        "tgt_lang": tgt_lang_code
    }
    payload.update(kwargs)
    resp = requests.post(
        url,
        headers={**client._headers(), "Content-Type": "application/json"},
        json=payload
    )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

class Chat:
    @staticmethod
    def create(prompt, src_lang, tgt_lang, **kwargs):
        from . import _get_client
        return _get_client().chat(prompt, src_lang, tgt_lang, **kwargs)