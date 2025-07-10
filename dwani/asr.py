from .exceptions import DwaniAPIError
import requests

# Allowed languages (case-sensitive for display, but we'll handle case-insensitively)
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
    "Telugu",
    "English",
    "German"
]

def validate_language(language):
    """Validate that the provided language is in the allowed list (case-insensitive)."""
    # Create a case-insensitive mapping of allowed languages
    language_map = {lang.lower(): lang for lang in ALLOWED_LANGUAGES}
    # Check if the lowercase version of the input language is in the map
    if language.lower() not in language_map:
        raise ValueError(
            f"Unsupported language: {language}. Supported languages: {ALLOWED_LANGUAGES}"
        )
    # Return the original case from ALLOWED_LANGUAGES for consistency
    return language_map[language.lower()]

def asr_transcribe(client, file_path, language):
    # Validate the language input (case-insensitive)
    validated_language = validate_language(language)
    
    # Convert language to lowercase for the API request
    api_language = validated_language.lower()
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(
            f"{client.api_base}/v1/transcribe/?language={api_language}",
            headers=client._headers(),
            files=files,
            timeout=90
        )
    if resp.status_code != 200:
        raise DwaniAPIError(resp)
    return resp.json()

class ASR:
    @staticmethod
    def transcribe(*args, **kwargs):
        from . import _get_client
        return _get_client().transcribe(*args, **kwargs)