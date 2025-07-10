from .exceptions import DwaniAPIError
import requests

def audio_speech(client, input, response_format="mp3", output_file=None, language="kannada"):
    params = {
        "input": input,
        "response_format": response_format,
        "language": language
    }
    resp = requests.post(
        f"{client.api_base}/v1/audio/speech",
        headers={**client._headers(), "accept": "application/json"},
        params=params,
        data='',  # Empty body, as in the curl example
        stream=True,
        timeout=90
    )
    if resp.status_code != 200:
        raise DwaniAPIError(resp)
    if output_file:
        with open(output_file, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return output_file
    return resp.content

class Audio:
    @staticmethod
    def speech(*args, **kwargs):
        from . import _get_client
        return _get_client().speech(*args, **kwargs)
