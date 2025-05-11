from .exceptions import DhwaniAPIError
import requests

def run_translate(client, sentences, src_lang, tgt_lang, **kwargs):
    url = f"{client.api_base}/v1/translate"
    payload = {
        "sentences": sentences,
        "src_lang": src_lang,
        "tgt_lang": tgt_lang
    }
    payload.update(kwargs)
    resp = requests.post(
        url,
        headers={**client._headers(), "Content-Type": "application/json", "accept": "application/json"},
        json=payload
    )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

class Translate:
    @staticmethod
    def translate(sentence, src_lang, tgt_lang, **kwargs):
        from . import _get_client
        client = _get_client()
        # Ensure sentences is always a list
        response = run_translate(client, [sentence], src_lang, tgt_lang, **kwargs)
        # Return the first translation, or None if not found
        return response.get("translations", [None])[0]
