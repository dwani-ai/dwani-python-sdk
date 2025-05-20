
import dwani
import os


dwani.api_key = os.getenv("DWANI_API_KEY")

dwani.api_base = os.getenv("DWANI_API_BASE_URL")

resp = dwani.Chat.create(prompt="Hello!", src_lang="english", tgt_lang="kannada")
print(resp)


result = dwani.Vision.caption(
    file_path="image.png",
    query="Describe this logo",
    src_lang="english",
    tgt_lang="kannada"
)
print(result)


result = dwani.ASR.transcribe(file_path="kannada_sample.wav", language="kannada")
print(result)



resp = dwani.Translate.run_translate(sentences=["hi"], src_lang="english", tgt_lang="kannada")
print(resp)


result = dwani.Documents.run_extract(file_path = "dwani-workshop.pdf", page_number=1, src_lang="english",tgt_lang="kannada" )
print(result)


result = dwani.Documents.summarize(file_path = "dwani-workshop.pdf", page_number=1, src_lang="english",tgt_lang="kannada" )
print(result)



result = dwani.Documents.run_doc_query(file_path = "dwani-workshop.pdf", prompt = "list the key points", page_number=1, src_lang="english",tgt_lang="kannada" )
print(result)


response = dwani.Audio.speech(input="ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="mp3")
with open("output.mp3", "wb") as f:
    f.write(response)
