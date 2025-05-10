from .exceptions import DhwaniAPIError
import requests
def asr_transcribe(client, file_path, language):
    with open(file_path, "rb") as f:
        files = {"file": f}
        resp = requests.post(
            f"{client.api_base}/v1/transcribe/?language={language}",
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

