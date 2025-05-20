from .exceptions import DhwaniAPIError
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
    ("Telugu", "tel_Telu") 
]

# Create dictionaries for language name to code and code to code mapping
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

def vision_caption(client, file_path, query="describe the image", src_lang="eng_Latn", tgt_lang="kan_Knda"):
    # Normalize source and target languages
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    # Build the endpoint using the client's api_base
    url = (
        f"{client.api_base}/v1/indic_visual_query"
        f"?src_lang={src_lang_code}&tgt_lang={tgt_lang_code}"
    )
    headers = {
        **client._headers(),
        "accept": "application/json"
    }
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "image/png")}
        data = {"query": query}
        resp = requests.post(
            url,
            headers=headers,
            files=files,
            data=data
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

class Vision:
    @staticmethod
    def caption(*args, **kwargs):
        from . import _get_client
        return _get_client().caption(*args, **kwargs)