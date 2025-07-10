import requests

from .exceptions import DwaniAPIError
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Language options mapping (aligned with server’s SUPPORTED_LANGUAGES)
language_options = [
    ("English", "eng_Latn"),
    ("Kannada", "kan_Knda"),
    ("Hindi", "hin_Deva"),
    ("Tamil", "tam_Taml"),
    ("Telugu", "tel_Telu"),
    ("German", "deu_Latn") 
]

# Create dictionaries for language name to code and code to code mapping
lang_name_to_code = {name.lower(): code for name, code in language_options}
lang_code_to_code = {code: code for _, code in language_options}

# Supported models (aligned with server)
VALID_MODELS = ["gemma3", "moondream", "qwen2.5vl", "qwen3", "sarvam-m", "deepseek-r1"]

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

def validate_model(model):
    """Validate the model against supported models."""
    if model not in VALID_MODELS:
        raise ValueError(f"Unsupported model: {model}. Supported models: {VALID_MODELS}")
    return model

def document_ocr_all(client, file_path, model="gemma3"):
    """OCR a document (image/PDF) and return extracted text."""
    logger.debug(f"Calling document_ocr: file_path={file_path}, model={model}")
    validate_model(model)
    
    data = {"model": model}

    with open(file_path, "rb") as f:
        mime_type = "application/pdf" if file_path.lower().endswith('.pdf') else "image/png"
        files = {"file": (file_path, f, mime_type)}
        try:
            resp = requests.post(
                f"{client.api_base}/v1/extract-text-all",
                headers=client._headers(),
                files=files,
                data=data,
                timeout=90
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"OCR request failed: {str(e)}")
            raise DwaniAPIError(resp) if 'resp' in locals() else DwaniAPIError.from_exception(e)
    
    logger.debug(f"OCR response: {resp.status_code}")
    return resp.json()


def document_ocr_number(client, file_path, page_number, model="gemma3"):
    """OCR a document (image/PDF) and return extracted text."""
    logger.debug(f"Calling document_ocr: file_path={file_path}, model={model}")
    validate_model(model)
    
    data = {"model": model,
            "page_number": page_number}
    
    params = {"model": data["model"], "page_number": data["page_number"]}
    with open(file_path, "rb") as f:
        mime_type = "application/pdf" if file_path.lower().endswith('.pdf') else "image/png"
        files = {"file": (file_path, f, mime_type)}
        try:
            resp = requests.post(
                f"{client.api_base}/v1/extract-text",
                headers=client._headers(),
                files=files,
                params=params,
                timeout=90
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"OCR request failed: {str(e)}")
            raise DwaniAPIError(resp) if 'resp' in locals() else DwaniAPIError.from_exception(e)
    
    logger.debug(f"OCR response: {resp.status_code}")
    return resp.json()
def document_summarize(client, file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
    """Summarize a PDF document with language and page number options."""
    logger.debug(f"Calling document_summarize: file_path={file_path}, page_number={page_number}, src_lang={src_lang}, tgt_lang={tgt_lang}, model={model}")
    validate_model(model)
    
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("File must be a PDF")
    if page_number < 1:
        raise ValueError("Page number must be at least 1")
    
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/indic-summarize-pdf"
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}
        data = {
            "page_number": str(page_number),
            "src_lang": src_lang_code,
            "tgt_lang": tgt_lang_code,
            "model": model
        }

        try:
            resp = requests.post(
                url,
                headers=headers,
                files=files,
                data=data,
                timeout=90
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Summarize request failed: {str(e)}")
            raise DwaniAPIError(resp) if 'resp' in locals() else DwaniAPIError.from_exception(e)
    
    logger.debug(f"Summarize response: {resp.status_code}")

    return resp.json()

def extract(client, file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
    """Extract and translate text from a PDF document using form data."""
    logger.debug(f"Calling extract: file_path={file_path}, page_number={page_number}, src_lang={src_lang}, tgt_lang={tgt_lang}, model={model}")
    validate_model(model)
    
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("File must be a PDF")
    if page_number < 1:
        raise ValueError("Page number must be at least 1")
    
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/indic-extract-text/"
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}

        data = {
            "page_number": str(page_number),
            "src_lang": src_lang_code,
            "tgt_lang": tgt_lang_code,
            "model": model
        }
        try:
            resp = requests.post(
                url,
                headers=headers,
                files=files,
                data=data,
                timeout=90
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Extract request failed: {str(e)}")
            raise DwaniAPIError(resp) if 'resp' in locals() else DwaniAPIError.from_exception(e)
    
    logger.debug(f"Extract response: {resp.status_code}")

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
    logger.debug(f"Calling doc_query: file_path={file_path}, page_number={page_number}, prompt={prompt}, src_lang={src_lang}, tgt_lang={tgt_lang}, model={model}")
    validate_model(model)
    
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("File must be a PDF")
    if page_number < 1:
        raise ValueError("Page number must be at least 1")
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/indic-custom-prompt-pdf"
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}
        data = {
            "page_number": str(page_number),
            "prompt": prompt,
            "src_lang": src_lang_code,
            "tgt_lang": tgt_lang_code,
            "model": model
        }

        try:
            resp = requests.post(
                url,
                headers=headers,
                files=files,
                data=data,
                timeout=90
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Doc query request failed: {str(e)}")
            raise DwaniAPIError(resp) if 'resp' in locals() else DwaniAPIError.from_exception(e)
    
    logger.debug(f"Doc query response: {resp.status_code}")

    return resp.json()

def doc_query_kannada(
    client,
    file_path,
    page_number=1,
    prompt="list key points",
    src_lang="eng_Latn",
    tgt_lang="kan_Knda",
    model="gemma3"
):
    """Query a document with a custom prompt, outputting in Kannada."""
    logger.debug(f"Calling doc_query_kannada: file_path={file_path}, page_number={page_number}, prompt={prompt}, src_lang={src_lang}, tgt_lang={tgt_lang}, model={model}")
    validate_model(model)
    
    if not file_path.lower().endswith('.pdf'):
        raise ValueError("File must be a PDF")
    if page_number < 1:
        raise ValueError("Page number must be at least 1")
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang) if tgt_lang else "kan_Knda"
    
    url = f"{client.api_base}/v1/indic-custom-prompt-pdf"
    headers = client._headers()
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/pdf")}

        data = {
            "page_number": str(page_number),
            "prompt": prompt,
            "src_lang": src_lang_code,
            "tgt_lang": tgt_lang_code,
            "model": model
        }
        try:
            resp = requests.post(
                url,
                headers=headers,
                files=files,
                data=data,
                timeout=90
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Doc query Kannada request failed: {str(e)}")
            raise DwaniAPIError(resp) if 'resp' in locals() else DwaniAPIError.from_exception(e)
    
    logger.debug(f"Doc query Kannada response: {resp.status_code}")

    return resp.json()

class Documents:
    @staticmethod
    def run_ocr_number(file_path, page_number=2,model="gemma3"):
        from .client import DwaniClient
        client = DwaniClient()
        return document_ocr_number(client, file_path, page_number, model)
    @staticmethod
    def run_ocr_all(file_path, model="gemma3"):
        from .client import DwaniClient
        client = DwaniClient()
        return document_ocr_all(client, file_path, model)
    
    @staticmethod
    def summarize(file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .client import DwaniClient
        client = DwaniClient()
        return document_summarize(client, file_path, page_number, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_extract(file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .client import DwaniClient
        client = DwaniClient()
        return extract(client, file_path, page_number, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_doc_query(file_path, page_number=1, prompt="list the key points", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .client import DwaniClient
        client = DwaniClient()
        return doc_query(client, file_path, page_number, prompt, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_doc_query_kannada(file_path, page_number=1, prompt="list key points", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .client import DwaniClient
        client = DwaniClient()
        return doc_query_kannada(client, file_path, page_number, prompt, src_lang, tgt_lang, model)