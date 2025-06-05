import requests
from .exceptions import DhwaniAPIError

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

def document_ocr(client, file_path, language=None, model="gemma3"):
    """OCR a document (image/PDF) and return extracted text."""
    # Validate model
    valid_models = ["gemma3", "moondream", "qwen2.5vl"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")
    
    data = {"model": model}
    if language:
        # Normalize the language input
        data["language"] = normalize_language(language)
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(
            f"{client.api_base}/v1/document/ocr",
            headers=client._headers(),
            files=files,
            data=data
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

def document_summarize(client, file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
    """Summarize a PDF document with language and page number options."""
    # Validate model
    valid_models = ["gemma3", "moondream", "qwen2.5vl"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")
    
    # Normalize source and target languages
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/indic-summarize-pdf"
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}
        data = {
            "page_number": str(page_number),
            "src_lang": src_lang_code,
            "tgt渊lang": tgt_lang_code,
            "model": model
        }
        resp = requests.post(
            url,
            headers=headers,
            files=files,
            data=data
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

def extract(client, file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
    """Extract and translate text from a document (image/PDF) using query parameters."""
    # Validate model
    valid_models = ["gemma3", "moondream", "qwen2.5vl"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")
    
    # Normalize source and target languages
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    # Build the URL with query parameters
    url = (
        f"{client.api_base}/v1/indic-extract-text/"
        f"?page_number={page_number}&src_lang={src_lang_code}&tgt_lang={tgt_lang_code}&model={model}"
    )
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}
        resp = requests.post(
            url,
            headers=headers,
            files=files
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

def doc_query(
    client,
    file_path,
    page_number=1,
    prompt="list the key points",
    src_lang="eng_Latn",
    tgt_lang="kan_Knda",
    model="gemma3"
):
    """Query a document with a custom prompt and language options."""
    # Validate model
    valid_models = ["gemma3", "moondream", "qwen2.5vl"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")
    
    # Normalize source and target languages
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/indic-custom-prompt-pdf"
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}
        data = {
            "page_number": str(page_number),
            "prompt": prompt,
            "source_language": src_lang_code,
            "target_language": tgt_lang_code,
            "model": model
        }
        resp = requests.post(
            url,
            headers=headers,
            files=files,
            data=data
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

def doc_query_kannada(
    client, 
    file_path, 
    page_number=1, 
    prompt="list key points", 
    src_lang="eng_Latn",
    language=None,
    model="gemma3"
):
    """Summarize a document (image/PDF/text) with custom prompt and language."""
    # Validate model
    valid_models = ["gemma3", "moondream", "qwen2.5vl"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")
    
    # Normalize source language and optional language parameter
    src_lang_code = normalize_language(src_lang)
    data = {
        "page_number": str(page_number),
        "prompt": prompt,
        "src_lang": src_lang_code,
        "model": model
    }
    if language:
        data["language"] = normalize_language(language)
    
    url = f"{client.api_base}/v1/indic-custom-prompt-kannada-pdf"
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}
        resp = requests.post(
            url,
            headers=headers,
            files=files,
            data=data
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

class Documents:
    @staticmethod
    def ocr(file_path, language=None, model="gemma3"):
        from . import _get_client
        return _get_client().document_ocr(file_path, language, model)
    
    @staticmethod
    def summarize(file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from . import _get_client
        return _get_client().document_summarize(file_path, page_number, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_extract(file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from . import _get_client
        return _get_client().extract(file_path, page_number, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_doc_query(file_path, page_number=1, prompt="list the key points", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from . import _get_client
        return _get_client().doc_query(file_path, page_number, prompt, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_doc_query_kannada(file_path, page_number=1, prompt="list key points", src_lang="eng_Latn", language=None, model="gemma3"):
        from . import _get_client
        return _get_client().doc_query_kannada(file_path, page_number, prompt, src_lang, language, model)