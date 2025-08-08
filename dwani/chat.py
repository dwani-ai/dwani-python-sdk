from .exceptions import DwaniAPIError
import requests
import re

# Language options mapping
language_options = [
    ("English", "eng_Latn"),
    ("Kannada", "kan_Knda"),
    ("Hindi", "hin_Deva"), 
    ("Assamese", "asm_Beng"),
    ("Bengali","ben_Beng"),
    ("Gujarati","guj_Gujr"),
    ("Malayalam","mal_Mlym"),
    ("Marathi","mar_Deva"),
    ("Odia","ory_Orya"),
    ("Punjabi","pan_Guru"),
    ("Tamil","tam_Taml"),
    ("Telugu","tel_Telu"),
    ("German","deu_Latn"),
]

# Create a dictionary for language name to code mapping
lang_name_to_code = {name.lower(): code for name, code in language_options}
lang_code_to_code = {code: code for _, code in language_options}

def normalize_language(lang):
    """Convert language input (name or code) to language code."""
    lang = lang.strip()
    # Check if input is a language name (case-insensitive)
    lang_lower = lang.lower()
    if lang_lower in lang_name_to_code:
        return lang_name_to_code[lang_lower]
    # Check if input is a language code
    if lang in lang_code_to_code:
        return lang_code_to_code[lang]
    # Raise error if language is not supported
    supported_langs = list(lang_name_to_code.keys()) + list(lang_code_to_code.keys())
    raise ValueError(f"Unsupported language: {lang}. Supported languages: {supported_langs}")

def chat_direct(client, prompt, model="gemma3", system_prompt=""):
    valid_models = ["gemma3", "qwen3", "gpt-oss", "sarvam-m"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")

    url = f"{client.api_base}/v1/chat_direct"
    payload = {
        "prompt": prompt,
        "model": model,
        "system_prompt":system_prompt
    }
    resp = requests.post(
        url,
        headers={**client._headers(), "Content-Type": "application/json"},
        json=payload,
        timeout=90
    )
    if resp.status_code != 200:
        raise DwaniAPIError(resp)
    return resp.json()

def chat_create(client, prompt, src_lang, tgt_lang, model="gemma3"):
    # Validate model
    valid_models = ["gemma3", "qwen3", "gpt-oss", "sarvam-m"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")
    
    # Normalize source and target languages
    src_lang_code = normalize_language(src_lang)
    tgt_lang_code = normalize_language(tgt_lang)
    
    url = f"{client.api_base}/v1/indic_chat"
    payload = {
        "prompt": prompt,
        "src_lang": src_lang_code,
        "tgt_lang": tgt_lang_code,
        "model": model
    }
    resp = requests.post(
        url,
        headers={**client._headers(), "Content-Type": "application/json"},
        json=payload,
        timeout=90
    )
    if resp.status_code != 200:
        raise DwaniAPIError(resp)
    return resp.json()

def chat_session(client, prompt, model="gemma3", system_prompt=""):
    valid_models = ["gemma3", "qwen3", "gpt-oss", "sarvam-m"]
    if model not in valid_models:
        raise ValueError(f"Unsupported model: {model}. Supported models: {valid_models}")

    url = f"{client.api_base}/v1/chat_session"
    payload = {
        "prompt": prompt,
        "model": model,
        "system_prompt":system_prompt
    }


    GPT_OSS_API_URL = os.getenv('GPT_OSS_API_URL', "http://localhost:9500/v1/chat/completions")
    resp = requests.post(GPT_OSS_API_URL, json=data, timeout=60)
    resp.raise_for_status()
    result = resp.json()

    # The raw content might be with special tokens, so extract final message
    raw_answer = result["choices"][0]["message"]["content"]
    final_message = get_final_message(raw_answer)
    answer = final_message if final_message is not None else raw_answer
    return answer

    resp = requests.post(
        url,
        headers={**client._headers(), "Content-Type": "application/json"},
        json=payload,
        timeout=90
    )
    if resp.status_code != 200:
        raise DwaniAPIError(resp)
    return resp.json()



"""





def extract_values(text):
    pattern = r'<\|channel\|>(.*?)<\|message\|>(.*?)(?=<\|start\|>|<\|channel\|>|$)'
    matches = re.findall(pattern, text, re.DOTALL)
    result = [{'channel': m[0], 'message': m[1].strip()} for m in matches]
    return result

def get_final_message(text):
    extracted = extract_values(text)
    for item in extracted:
        if item['channel'] == 'final':
            return item['message']
    return None  # Return None if no "final" message found

def ask_gpt(user_message, history):
    # Compose conversation history to OpenAI format
    messages = [{"role": "system", "content": "hello"}]  # Optional system prompt

    for user, assistant in history:
        messages.append({"role": "user", "content": user})
        if assistant:
            messages.append({"role": "assistant", "content": assistant})

    # Add the new user message
    messages.append({"role": "user", "content": user_message})

    data = {
        "messages": messages,
        "temperature": 1.0,
        "max_tokens": 1000,
        "stream": False,
        "model": "openai/gpt-oss-120b"
    }

    try:
        resp = requests.post(GPT_OSS_API_URL, json=data, timeout=60)
        resp.raise_for_status()
        result = resp.json()

        # The raw content might be with special tokens, so extract final message
        raw_answer = result["choices"][0]["message"]["content"]
        final_message = get_final_message(raw_answer)
        answer = final_message if final_message is not None else raw_answer
    except Exception as e:
        answer = f"Error: {e}"
    return answer


"""

class Chat:
    @staticmethod
    def create(prompt, src_lang, tgt_lang, model="gemma3"):
        from . import _get_client
        return _get_client().chat(prompt, src_lang, tgt_lang, model)
    @staticmethod
    def direct(prompt, model="gemma3", system_prompt=""):
        from . import _get_client
        return _get_client().chat_direct(prompt, model, system_prompt)