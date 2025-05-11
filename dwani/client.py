import os
import requests
from .exceptions import DhwaniAPIError

class DhwaniClient:
    def __init__(self, api_key=None, api_base=None):
        self.api_key = api_key or os.getenv("DWANI_API_KEY")
        self.api_base = api_base or os.getenv("DWANI_API_BASE_URL", "http://localhost:8000")
        if not self.api_key:
            raise ValueError("DHWANI_API_KEY not set")

    def _headers(self):
        return {"X-API-Key": self.api_key}

    def chat(self, prompt, src_lang, tgt_lang, **kwargs):
        from .chat import chat_create
        return chat_create(self, prompt, src_lang, tgt_lang, **kwargs)
    
    def translate(self, sentences, src_lang, tgt_lang, **kwargs):
        from .translate import run_translate
        return run_translate(self, sentences=sentences,src_lang= src_lang, tgt_lang=tgt_lang, **kwargs)

    def speech(self, *args, **kwargs):
        from .audio import audio_speech
        return audio_speech(self, *args, **kwargs)

    def caption(self, file_path, query="describe the image", src_lang="eng_Latn", tgt_lang="kan_Knda"):
        from .vision import vision_caption
        return vision_caption(self, file_path, query, src_lang, tgt_lang)

    def transcribe(self, *args, **kwargs):
        from .asr import asr_transcribe
        return asr_transcribe(self, *args, **kwargs)
    
    def document_ocr(self, file_path, language=None):
        from .docs import document_ocr
        return document_ocr(self, file_path, language)

    def document_translate(self, file_path, src_lang, tgt_lang):
        from .docs import document_translate
        return document_translate(self, file_path, src_lang, tgt_lang)

    def document_summarize(self, file_path, language=None):
        from .docs import document_summarize
        return document_summarize(self, file_path, language)

