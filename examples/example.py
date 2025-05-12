
import dwani
import os


dwani.api_key = os.getenv("DWANI_API_KEY")

dwani.api_base = os.getenv("DWANI_API_BASE_URL")

resp = dwani.Chat.create(prompt="Hello!", src_lang="eng_Latn", tgt_lang="kan_Knda")
print(resp)


result = dwani.Vision.caption(
    file_path="image.png",
    query="Describe this logo",
    src_lang="eng_Latn",
    tgt_lang="kan_Knda"
)
print(result)


result = dwani.ASR.transcribe(file_path="kannada_sample.wav", language="kannada")
print(result)


response = dwani.Audio.speech(input="ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="mp3")
with open("output.mp3", "wb") as f:
    f.write(response)

resp = dwani.Translate.run_translate(sentences=["hi"], src_lang="eng_Latn", tgt_lang="kan_Knda")
print(resp)


result = dwani.Documents.run_doc_query_kannada(file_path = "dwani-workshop.pdf", page_number=1, prompt="list key points", src_lang="eng_Latn" )
print(result)
