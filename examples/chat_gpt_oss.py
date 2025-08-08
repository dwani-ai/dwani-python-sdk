import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")


resp = dwani.Chat.direct(prompt="Hello!", model="gemma3")
print("Chat: Gemma3 - ", resp)



resp = dwani.Chat.direct(prompt="Hello!", model="gpt-oss")
print("Chat: gpt-oss - ", resp)
