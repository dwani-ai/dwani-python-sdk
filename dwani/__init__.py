from .client import DwaniClient
from .chat import Chat
from .audio import Audio
from .vision import Vision
from .asr import ASR
from .translate import Translate
from .exceptions import DwaniAPIError
from .docs import Documents

__all__ = ["DwaniClient", "Chat", "Audio", "Vision", "ASR", "DwaniAPIError", "Translate", "Documents"]

# Optionally, instantiate a default client for convenience
api_key = None
api_base = "http://0.0.0.0:8000"

def _get_client():
    global _client
    if "_client" not in globals() or _client is None:
        from .client import DwaniClient
        globals()["_client"] = DwaniClient(api_key=api_key, api_base=api_base)
    return _client

class chat:
    @staticmethod
    def create(prompt, src_lang, tgt_lang, model="gemma3"):
        return _get_client().chat(prompt, src_lang, tgt_lang, model)
    @staticmethod
    def direct(prompt, model="gemma3", system_prompt =""):
        return _get_client().chat_direct(prompt, model, system_prompt)

class audio:
    @staticmethod
    def speech(input, response_format="wav", language="kannada"):
        return _get_client().speech(input, response_format, language)

class vision:
    @staticmethod
    def caption(file_path, query="describe the image", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        return _get_client().caption(file_path, query, src_lang, tgt_lang, model)
    @staticmethod
    def caption_direct(file_path, query="describe the image", model="gemma3", system_prompt=""):
        return _get_client().caption_direct(file_path, query, model, system_prompt)

class asr:
    @staticmethod
    def transcribe(file_path, language="kannada"):
        return _get_client().transcribe(file_path, language)

class translate:
    @staticmethod
    def run_translate(sentences, src_lang="kan_Knda", tgt_lang="eng_Latn"):
        return _get_client().translate(sentences, src_lang, tgt_lang)

class document:
    @staticmethod
    def run_ocr_number(file_path, page_number=1, model="gemma3"):
        return _get_client().document_ocr_number(file_path, page_number, model)
    
    @staticmethod
    def run_ocr_all(file_path, model="gemma3"):
        return _get_client().document_ocr_all(file_path, model)
    
    @staticmethod
    def run_summarize(file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        return _get_client().document_summarize(file_path, page_number, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_extract(file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        return _get_client().extract(file_path, page_number, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_doc_query(file_path, page_number=1, prompt="list the key points", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        return _get_client().doc_query(file_path, page_number, prompt, src_lang, tgt_lang, model)
    
    @staticmethod
    def run_doc_query_kannada(file_path, page_number=1, prompt="list key points", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        return _get_client().doc_query_kannada(file_path, page_number, prompt, src_lang, tgt_lang, model)