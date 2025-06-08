# dwani.ai - python library


### Install the library
```bash
pip install --upgrade dwani
```

### Languages supported
    - Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu

### Setup the credentials
```python
import dwani
import os

dwani.api_key = os.getenv("DWANI_API_KEY")

dwani.api_base = os.getenv("DWANI_API_BASE_URL")
```


### Text Query 
---
- With model selection
  - gemma3 (default), qwen3, sarvam-m

---
- gemma3 - with translation
```python
resp = dwani.Chat.create(prompt="Hello!", src_lang="english", tgt_lang="kannada", model="gemma3")
print(resp)
```
```json
{'response': 'ನಮಸ್ತೆ! ಭಾರತ ಮತ್ತು ಕರ್ನಾಟಕವನ್ನು ಗಮನದಲ್ಲಿಟ್ಟುಕೊಂಡು ಇಂದು ನಿಮ್ಮ ಪ್ರಶ್ನೆಗಳಿಗೆ ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಲಿ?'}
```

- gemma3 - without translation
```python
resp = dwani.Chat.direct(prompt="Hello!", model="gemma3")
print(resp)
```
```json
{'response': 'Hello! I am Dwani, ready to assist you with information pertaining to India, specifically Karnataka. '}
```

---
### Vision Query
---
- With model selection
  - gemma3 (default), moondream, smolvla

- gemma3 - with translation
```python
result = dwani.Vision.caption(
    file_path="image.png",
    query="Describe this logo",
    src_lang="english",
    tgt_lang="kannada",
    model="gemma3"
)
print(result)
```
```json
{'answer': 'ಒಂದು ವಾಕ್ಯದಲ್ಲಿ ಚಿತ್ರದ ಸಾರಾಂಶವನ್ನು ಇಲ್ಲಿ ನೀಡಲಾಗಿದೆಃ ಪ್ರಕಟಣೆಯ ಅವಲೋಕನವು ಪ್ರಸ್ತುತ ಅರವತ್ತನಾಲ್ಕು ದೇಶಗಳು/ಪ್ರದೇಶಗಳನ್ನು ಸೇರಿಸಲಾಗಿದೆ ಮತ್ತು ಇನ್ನೂ ಹದಿನಾರು ಪ್ರದೇಶಗಳನ್ನು ಸೇರಿಸಬೇಕಾಗಿದೆ. ಒದಗಿಸಲಾದ ಚಿತ್ರದಲ್ಲಿ ಲಾಂಛನವು ಕಾಣಿಸುವುದಿಲ್ಲ.'}
```
- gemma3 - without translation
```python
result = dwani.Vision.caption_direct(
    file_path="image.png",
    query="Describe this logo",
    model="gemma3"
)
print(result)
```
```json
 {'answer': 'The logo displays a publishing overview stating that changes are under review, with a production rollout initiated at version sixty-four point one point one, expanding to sixteen countries/regions including Australia and Bangladesh.'}
```

---
### Speech to Text -  Automatic Speech Recognition (ASR)
---
```python
result = dwani.ASR.transcribe(file_path="kannada_sample.wav", language="kannada")
print(result)
```
```json
{'text': 'ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು'}
```
---
### Translate
---
```python
resp = dwani.Translate.run_translate(sentences="hi, i am gaganyatri", src_lang="english", tgt_lang="kannada")
print(resp)
```
```json
{'translations': ['ಹಾಯ್, ನಾನು ಗಗನಯಾತ್ರಿ']}
```
---
### Text to Speech -  Speech Synthesis
---
```python
response = dwani.Audio.speech(input="ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="wav")
with open("output.wav", "wb") as f:
    f.write(response)
```

#### Document - Extract Text
```python
result = dwani.Documents.run_extract(file_path = "dwani-workshop.pdf", page_number=1, src_lang="english",tgt_lang="kannada" )
print(result)
```
```json
{'pages': [{'processed_page': 1, 'page_content': ' a plain text representation of the document', 'translated_content': 'ಡಾಕ್ಯುಮೆಂಟ್ನ ಸರಳ ಪಠ್ಯ ಪ್ರಾತಿನಿಧ್ಯವನ್ನು ಇಲ್ಲಿ ನೀಡಲಾಗಿದೆ, ಅದನ್ನು ಸ್ವಾಭಾವಿಕವಾಗಿ ಓದುವಂತೆಃ'}]}
```

- Website -> [dwani.ai](https://dwani.ai)


<!-- 
## local development
pip install -e .


pip install twine build
rm -rf dist/
python -m build

python -m twine upload dist/*

-->