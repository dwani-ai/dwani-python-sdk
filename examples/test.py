import dwani

import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")



result = dwani.Vision.caption_direct(
            file_path="sample_data/image.png",
            query="Describe this image",
            model="gemma3"
        )
print("Vision Response: ", result)