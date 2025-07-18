import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")



result = dwani.Documents.query_page(
            file_path="olmocr-paper.pdf", model="gemma3", page_number=5, tgt_lang="kannada"
        )

print("Document Query Response: gemma3- ", result["translated_query_answer"])

print("------------")
result = dwani.Documents.query_page(
            file_path="olmocr-paper.pdf", model="gemma3", page_number=5
        )


print("Document Query Response: gemma3- ", result["translated_query_answer"])

print("------------")

result = dwani.Documents.query_all(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3", tgt_lang="kan_Knda"
        )
print("------------")

print("Document Query Response: gemma3- ", result["translated_query_answer"])