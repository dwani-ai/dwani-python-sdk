
import dwani
import os

dwani.api_key = os.getenv("DWANI_API_KEY")

dwani.api_base = os.getenv("DWANI_API_BASE")

resp = dwani.Chat.create("Hello!", "eng_Latn", "kan_Knda")
print(resp)


result = dwani.Vision.caption(
    file_path="image.png",
    query="Describe this logo",
    src_lang="eng_Latn",
    tgt_lang="kan_Knda"
)
print(result)


result = dwani.ASR.transcribe("kannada_sample.wav", "kannada")
print(result)

