# dwani.ai - python library


```bash
pip install dwani
```



```python
import dwani
import os

dwani.api_key = os.getenv("DWANI_API_KEY")

dwani.api_base = os.getenv("DWANI_API_BASE_URL")

resp = dwani.Chat.create("Hello!", "eng_Latn", "kan_Knda")
print(resp)
```


<!-- 
## local development
pip install -e .


pip install twine build
rm -rf dist/
python -m build

python -m twine upload dist/*

-->