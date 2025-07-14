import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")

'''

result = dwani.Documents.run_ocr_number(
            file_path="olmocr-paper.pdf", model="gemma3", page_number=5
        )


print("Document Query Response: gemma3- ", result)

print("------------")
result = dwani.Documents.run_ocr_number(
            file_path="olmocr-paper.pdf", model="gemma3", page_number=2
        )

print("Document Query Response: gemma3- ", result)

print("------------")

result = dwani.Documents.run_ocr_number(
            file_path="olmocr-paper.pdf", model="gemma3", page_number=3
        )

print("Document Query Response: gemma3- ", result)

print("------------")
result = dwani.Documents.run_ocr_all(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3"
        )


result = dwani.Documents.run_ocr_all(
            file_path="dwani-workshop.pdf", model="gemma3"
        )

result = dwani.Documents.run_ocr_all(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3"
        )
print("Document Query Response: gemma3- ", result)

'''

'''

result = dwani.Documents.summarize_page(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3" , page_number= 1
        )
print("Document Query Response: gemma3- ", result)



result = dwani.Documents.summarize_page(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3" , page_number= 3, tgt_lang="english"
        )
print("Document Query Response: gemma3- ", result)

result = dwani.Documents.summarize_page(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3" , page_number= 4 , tgt_lang="english"
        )
print("Document Query Response: gemma3- ", result)

result = dwani.Documents.summarize_page(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3" , page_number= 8 , tgt_lang="english"
        )
print("Document Query Response: gemma3- ", result)

'''
result = dwani.Documents.summarize_all(
            file_path="dwani-ai-pitch-deck.pdf", model="gemma3" , tgt_lang="english"
        )
#print("Document Query Response: gemma3- ", result)

#print("Document Query Response: gemma3- ", result["translated_summary"])


print("Document Query Response: gemma3- ", result["summary"])

result = dwani.Documents.summarize_all(
            file_path="sample_resume.pdf", model="gemma3" , tgt_lang="english"
  
    )

print("Document Query Response: gemma3- ", result["translated_summary"])

#print("Document Query Response: gemma3- ", result)

#print("Document Query Response: gemma3- ", result["summary"])

#print("Document Query Response: gemma3- ", result["translated_summary"])


print("Document Query Response: gemma3- ", result["summary"])

result = dwani.Documents.summarize_all(
            file_path="dwani-workshop.pdf", model="gemma3" , tgt_lang="english"  
    )


print("Document Query Response: gemma3- ", result["summary"])



result = dwani.Documents.summarize_all(
            file_path="olmocr-paper.pdf", model="gemma3" , tgt_lang="english"  
    )


print("Document Query Response: gemma3- ", result["summary"])

