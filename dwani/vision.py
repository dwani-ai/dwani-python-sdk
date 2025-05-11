from .exceptions import DhwaniAPIError
import requests
def vision_caption(client, file_path, query="describe the image", src_lang="eng_Latn", tgt_lang="kan_Knda"):
    # Build the endpoint using the client's api_base
    url = (
        f"{client.api_base}/v1/indic_visual_query"
        f"?src_lang={src_lang}&tgt_lang={tgt_lang}"
    )
    headers = {
        **client._headers(),
        "accept": "application/json"
        # Note: 'Content-Type' will be set automatically by requests when using 'files'
    }
    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "image/png")}
        data = {"query": query}
        resp = requests.post(
            url,
            headers=headers,
            files=files,
            data=data
        )
    if resp.status_code != 200:
        raise DhwaniAPIError(resp)
    return resp.json()

class Vision:
    @staticmethod
    def caption(*args, **kwargs):
        from . import _get_client
        return _get_client().caption(*args, **kwargs)
