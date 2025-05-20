from .exceptions import DhwaniAPIError
import requests

# Allowed languages (case-sensitive)
ALLOWED_LANGUAGES = [
    "Assamese",
    "Bengali",
    "Gujarati",
    "Hindi",
    "Kannada",
    "Malayalam",
    "Marathi",
    "Odia",
    "Punjabi",
    "Tamil",
    "Telugu"
]

def validate_language(language):
    """Validate that the provided language is in the allowed list (case-sensitive)."""
    if language not in ALLOWED_LANGUAGES:
        raise ValueError(
            f"Unsupported language: {language}. Supported languages: {ALLOWED_LANGUAGES}"
        )
    return language

def asr_transcribe(client, file_path, language):
    # Validate the language input (case-sensitive)
    validate_language(language)
    
    # Convert language to lowercase for the API request
    api_language = language.lower()
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(
            f"{client.api_base}/v1/transcribe/?language={api_language}",
            headers=client._headers(),
            files=files
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

class ASR:
    @staticmethod
    def transcribe(*args, **kwargs):
        from . import _get_client
        return _get_client().transcribe(*args, **kwargs)