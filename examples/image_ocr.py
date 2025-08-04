import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")

result = dwani.Vision.ocr_image(
            file_path="image.png", model="gemma3"
        )
print("Document Query Response: gemma3- ", result)
        