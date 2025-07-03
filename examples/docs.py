import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")


def run_doc_extract():
    try:
        result = dwani.Documents.run_extract(
            file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada"
        )
        print("Document Extract Response: default/gemma3- ", result)
        '''
        result = dwani.Documents.run_extract(
            file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada", model="gemma3"
        )
        print("Document Extract Response: gemma3- ", result)
        result = dwani.Documents.run_extract(
            file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada", model="moondream"
        )
        print("Document Extract Response: moondream- ", result)
        '''
    except Exception as e:
        print(f"Error in Document Extract module: {e}")

def run_doc_summarize():
    try:
        result = dwani.Documents.summarize(
            file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada"
        )
        print("Document Summarize Response: default/gemma3- ", result)
        '''
        result = dwani.Documents.summarize(
            file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada", model="gemma3"
        )
        print("Document Summarize Response: gemma3- ", result)
        result = dwani.Documents.summarize(
            file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada", model="moondream"
        )
        print("Document Summarize Response: moondream- ", result)
        '''
    except Exception as e:
        print(f"Error in Document Summarize module: {e}")

def run_doc_query():
    try:
        result = dwani.Documents.run_doc_query(
            file_path="dwani-workshop.pdf", prompt="list the key points",
            page_number=1, src_lang="english", tgt_lang="kannada", model="gemma3"
        )
        print("Document Query Response: gemma3- ", result)
        '''
        result = dwani.Documents.run_doc_query(
            file_path="dwani-workshop.pdf", prompt="list the key points",
            page_number=1, src_lang="english", tgt_lang="kannada", model="moondream"
        )
        print("Document Query Response: moondream3- ", result)
        '''
    except Exception as e:
        print(f"Error in Document Query module: {e}")


def run_doc_ocr():
    try:
        result = dwani.Documents.run_ocr(
            file_path="dwani-workshop.pdf", model="gemma3"
        )
        print("Document Query Response: gemma3- ", result)
        '''
        result = dwani.Documents.run_doc_query(
            file_path="dwani-workshop.pdf", prompt="list the key points",
            page_number=1, src_lang="english", tgt_lang="kannada", model="moondream"
        )
        print("Document Query Response: moondream3- ", result)
        '''
    except Exception as e:
        print(f"Error in Document Query module: {e}")

def run_all_modules():
    print("\nRunning all modules...")
    run_doc_extract()
    run_doc_ocr()
    run_doc_summarize()
    run_doc_query()

def display_menu():
    print("\ndwani.ai Docs API Module Selector")
    print("1. Document Extract")
    print("2. Document Summarize")
    print("3. Document Query")
    print("4. Document OCR")
    print("5. Run All Modules")
    print("0. Exit")
    return input("Enter your choice (0-9, default is 1): ").strip()

def main():
    while True:
        choice = display_menu()

        # Default to Chat if no input or invalid input
        if not choice or choice not in {"0", "1", "2", "3", "4", "5"}:
            choice = "1"

        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            run_doc_extract()
        elif choice == "2":
            run_doc_summarize()
        elif choice == "3":
            run_doc_query()
        elif choice == "4":
            run_doc_ocr()
        elif choice == "5":
            run_all_modules()

if __name__ == "__main__":
    main()