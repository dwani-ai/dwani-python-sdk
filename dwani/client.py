import os
import requests
from .exceptions import DwaniAPIError

class DwaniClient:
    def __init__(self, api_key=None, api_base=None):
        self.api_key = api_key or os.getenv("DWANI_API_KEY")
        self.api_base = api_base or os.getenv("DWANI_API_BASE_URL", "http://0.0.0.0:8000")
        if not self.api_key:
            raise ValueError("DWANI_API_KEY not set")

    def _headers(self):
        return {
            "X-API-Key": self.api_key,
            "Accept": "application/json"
        }

    def translate(self, sentences, src_lang, tgt_lang):
        from .translate import run_translate
        return run_translate(self, sentences=sentences, src_lang=src_lang, tgt_lang=tgt_lang)

    def chat(self, prompt, src_lang, tgt_lang, model="gemma3"):
        from .chat import chat_create
        return chat_create(self, prompt=prompt, src_lang=src_lang, tgt_lang=tgt_lang, model=model)

    def chat_direct(self, prompt, model="gemma3", system_prompt=""):
        from .chat import chat_direct
        return chat_direct(self, prompt=prompt, model=model, system_prompt=system_prompt)

    def speech(self, input, response_format="wav", language="kannada"):
        from .audio import audio_speech
        return audio_speech(self, input=input, response_format=response_format, language=language)

    def caption(self, file_path, query="describe the image", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .vision import vision_caption
        return vision_caption(self, file_path=file_path, query=query, src_lang=src_lang, tgt_lang=tgt_lang, model=model)

    def caption_direct(self, file_path, query="describe the image", model="gemma3", system_prompt=""):
        from .vision import vision_direct
        return vision_direct(self, file_path=file_path, query=query, model=model, system_prompt=system_prompt)

    def transcribe(self, file_path, language=None):
        from .asr import asr_transcribe
        return asr_transcribe(self, file_path=file_path, language=language)
    
    def document_ocr_number(self, file_path, page_number=1,model="gemma3"):
        from .docs import document_ocr_number
        return document_ocr_number(self, file_path=file_path, page_number=page_number, model=model)

    def document_ocr_all(self, file_path,model="gemma3"):
        from .docs import document_ocr_all
        return document_ocr_all(self, file_path=file_path, model=model)

    def document_summarize(self, file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .docs import document_summarize
        return document_summarize(self, file_path, page_number, src_lang, tgt_lang, model)

    def extract(self, file_path, page_number=1, src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .docs import extract
        return extract(self, file_path=file_path, page_number=page_number, src_lang=src_lang, tgt_lang=tgt_lang, model=model)

    def doc_query(self, file_path, page_number=1, prompt="list the key points", src_lang="eng_Latn", tgt_lang="kan_Knda", model="gemma3"):
        from .docs import doc_query
        return doc_query(self, file_path, page_number=page_number, prompt=prompt, src_lang=src_lang, tgt_lang=tgt_lang, model=model)

    def doc_query_kannada(self, file_path, page_number=1, prompt="list key points", src_lang="eng_Latn", language="kan_Knda", model="gemma3"):
        from .docs import doc_query_kannada
        return doc_query_kannada(self, file_path=file_path, page_number=page_number, prompt=prompt, src_lang=src_lang, language=language, model=model)