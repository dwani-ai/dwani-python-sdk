# dwani.ai - python library


### Install the library
```bash
pip install dwani
```

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

#### Speech to Text -  Automatic Speech Recognition (ASR)
```python
result = dwani.ASR.transcribe(file_path="kannada_sample.wav", language="kannada")
print(result)
```

#### Text to Speech -  Speech Synthesis

```python
response = dwani.Audio.speech(input="ಕರ್ನಾಟಕ ದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="mp3")
with open("output.mp3", "wb") as f:
    f.write(response)
```



- Website -> [dwani.ai](https://dwani.ai)



#### Contact
- For any questions or issues, please open an issue on GitHub or contact us via email.
- For collaborations
  - Join the discord group - [invite link](https://discord.gg/WZMCerEZ2P) 
<!-- 
## local development
pip install -e .


pip install twine build
rm -rf dist/
python -m build

python -m twine upload dist/*

-->