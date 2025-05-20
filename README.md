# dwani.ai - python library


### Install the library
```bash
pip install dwani
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

### Examples

#### Text Query 
```python
resp = dwani.Chat.create(prompt="Hello!", src_lang="eng_Latn", tgt_lang="kan_Knda")
print(resp)
```
```json
{'response': 'ನಮಸ್ತೆ! ಭಾರತ ಮತ್ತು ಕರ್ನಾಟಕವನ್ನು ಗಮನದಲ್ಲಿಟ್ಟುಕೊಂಡು ಇಂದು ನಿಮ್ಮ ಪ್ರಶ್ನೆಗಳಿಗೆ ನಾನು ನಿಮಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಲಿ?'}
```


#### Vision Query
```python
result = dwani.Vision.caption(
    file_path="image.png",
    query="Describe this logo",
    src_lang="eng_Latn",
    tgt_lang="kan_Knda"
)
print(result)
```
```json
{'answer': 'ಒಂದು ವಾಕ್ಯದಲ್ಲಿ ಚಿತ್ರದ ಸಾರಾಂಶವನ್ನು ಇಲ್ಲಿ ನೀಡಲಾಗಿದೆಃ ಪ್ರಕಟಣೆಯ ಅವಲೋಕನವು ಪ್ರಸ್ತುತ ಅರವತ್ತನಾಲ್ಕು ದೇಶಗಳು/ಪ್ರದೇಶಗಳನ್ನು ಸೇರಿಸಲಾಗಿದೆ ಮತ್ತು ಇನ್ನೂ ಹದಿನಾರು ಪ್ರದೇಶಗಳನ್ನು ಸೇರಿಸಬೇಕಾಗಿದೆ. ಒದಗಿಸಲಾದ ಚಿತ್ರದಲ್ಲಿ ಲಾಂಛನವು ಕಾಣಿಸುವುದಿಲ್ಲ.'}
```

#### Speech to Text -  Automatic Speech Recognition (ASR)
```python
result = dwani.ASR.transcribe(file_path="kannada_sample.wav", language="kannada")
print(result)
```
```json
{'text': 'ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು'}
```

### Translate
```python
resp = dwani.Translate.run_translate(sentences=["hi"], src_lang="eng_Latn", tgt_lang="kan_Knda")
print(resp)
```
```json
{'translations': ['ಹಾಯ್']}
```
#### Text to Speech -  Speech Synthesis

```python
response = dwani.Audio.speech(input="ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="mp3")
with open("output.mp3", "wb") as f:
    f.write(response)
```

#### Document - Extract Text
```python
result = dwani.Documents.run_extract(file_path = "dwani-workshop.pdf", page_number=1, src_lang="eng_Latn",tgt_lang="kan_Knda" )
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

    Assamese - asm_Beng , Bengali - ben_Beng, Gujarati - guj_Gujr, Hindi - hin_Deva, Kannada - kan_Knda, Malayalam - mal_Mlym, Marathi - mar_Deva, Odia -ory_Orya, Punjabi - pan_Guru , Tamil - tam_Taml, Telugu - tel_Telu


   <td>Assamese (asm_Beng)</td>
    <td>Kashmiri (Arabic) (kas_Arab)</td>
    <td>Punjabi (pan_Guru)</td>
  </tr>
  <tr>
    <td>Bengali (ben_Beng)</td>
    <td>Kashmiri (Devanagari) (kas_Deva)</td>
    <td>Sanskrit (san_Deva)</td>
  </tr>
  <tr>
    <td>Bodo (brx_Deva)</td>
    <td>Maithili (mai_Deva)</td>
    <td>Santali (sat_Olck)</td>
  </tr>
  <tr>
    <td>Dogri (doi_Deva)</td>
    <td>Malayalam (mal_Mlym)</td>
    <td>Sindhi (Arabic) (snd_Arab)</td>
  </tr>
  <tr>
    <td>English (eng_Latn)</td>
    <td>Marathi (mar_Deva)</td>
    <td>Sindhi (Devanagari) (snd_Deva)</td>
  </tr>
  <tr>
    <td>Konkani (gom_Deva)</td>
    <td>Manipuri (Bengali) (mni_Beng)</td>
    <td>Tamil (tam_Taml)</td>
  </tr>
  <tr>
    <td>Gujarati (guj_Gujr)</td>
    <td>Manipuri (Meitei) (mni_Mtei)</td>
    <td>Telugu (tel_Telu)</td>
  </tr>
  <tr>
    <td>Hindi (hin_Deva)</td>
    <td>Nepali (npi_Deva)</td>
    <td>Urdu (urd_Arab)</td>
  </tr>
  <tr>
    <td>Kannada (kan_Knda)</td>
    <td>Odia (ory_Orya)</td>
    <td></td>
    Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu
-->