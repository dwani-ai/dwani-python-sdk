import time
import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")

# Function to measure latency of each call
def measure_latency(func, *args, **kwargs):
    start_time = time.time()  # Start timer
    result = func(*args, **kwargs)  # Execute the function
    end_time = time.time()  # End timer
    latency = end_time - start_time  # Calculate latency
    print(f"Latency for {func.__name__}: {latency:.4f} seconds")
    return result  # Return the result of the API call

# Function for each module with latency measurement
def run_chat():
    try:
        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada")
        print("Chat Response: default/gemma3- ", resp)

        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada", model="qwen3")
        print("Chat Response: qwen3- ", resp)

        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada", model="gemma3")
        print("Chat Response: gemma3- ", resp)

        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada", model="sarvam-m")
        print("Chat Response: sarvam-m- ", resp)

        resp = measure_latency(dwani.Chat.direct, prompt="Hello!", model="qwen3")
        print("Chat Response: qwen3/direct- ", resp)

        resp = measure_latency(dwani.Chat.direct, prompt="Hello!", model="gemma3")
        print("Chat Response: gemma3/direct- ", resp)

        resp = measure_latency(dwani.Chat.direct, prompt="Hello!", model="sarvam-m")
        print("Chat Response: sarvam-m/direct- ", resp)

    except Exception as e:
        print(f"Error in Chat module: {e}")

def run_vision():
    try:
        result = measure_latency(dwani.Vision.caption, file_path="image.png", query="Describe this logo", src_lang="english", tgt_lang="kannada", model="gemma3")
        print("Vision Response: gemma3- ", result)

        result = measure_latency(dwani.Vision.caption, file_path="image.png", query="Describe this logo", src_lang="english", tgt_lang="kannada", model="moondream")
        print("Vision Response: moondream- ", result)

        result = measure_latency(dwani.Vision.caption_direct, file_path="image.png", query="Describe this logo", model="gemma3")
        print("Vision Response: gemma3/direct- ", result)

        result = measure_latency(dwani.Vision.caption_direct, file_path="image.png", query="Describe this logo", model="moondream")
        print("Vision Response: moondream/direct- ", result)

    except Exception as e:
        print(f"Error in Vision module: {e}")

def run_asr():
    try:
        result = measure_latency(dwani.ASR.transcribe, file_path="kannada_sample.wav", language="kannada")
        print("ASR Response:", result)
    except Exception as e:
        print(f"Error in ASR module: {e}")

def run_translate():
    try:
        # List of strings input
        resp = measure_latency(dwani.Translate.run_translate, sentences=["hi", "what is this?"], src_lang="english", tgt_lang="kannada")
        print("Translate Response:", resp)

        # Single string input
        resp = measure_latency(dwani.Translate.run_translate, sentences="hi, i am gaganyatri", src_lang="english", tgt_lang="kannada")
        print("Translate Response:", resp)

        # Open the file in read mode
        file_path = 'translation_large_content.txt'  # Replace with your file path

        with open(file_path, 'r') as file:
            text = file.read()

        resp = measure_latency(dwani.Translate.run_translate, sentences=text, src_lang="kannada", tgt_lang="english")
        print("Translate Response:", resp)

    except Exception as e:
        print(f"Error in Translate module: {e}")

def run_doc_extract():
    try:
        result = measure_latency(dwani.Documents.run_extract, file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada")
        print("Document Extract Response: ", result)

        result = measure_latency(dwani.Documents.run_extract, file_path="paper_1.pdf", page_number=1, src_lang="english", tgt_lang="kannada")
        print("Document Extract Response: ", result)

    except Exception as e:
        print(f"Error in Document Extract module: {e}")

def run_doc_summarize():
    try:
        result = measure_latency(dwani.Documents.summarize, file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada")
        print("Document Summarize Response: default/gemma3- ", result)

    except Exception as e:
        print(f"Error in Document Summarize module: {e}")

def run_doc_query():
    try:
        result = measure_latency(dwani.Documents.run_doc_query, file_path="dwani-workshop.pdf", prompt="list the key points", page_number=1, src_lang="english", tgt_lang="kannada", model="gemma3")
        print("Document Query Response: gemma3- ", result)

        result = measure_latency(dwani.Documents.run_doc_query, file_path="paper_1.pdf", prompt="list the key points", page_number=1, src_lang="english", tgt_lang="kannada", model="gemma3")
        print("Document Query Response: gemma3- ", result)

    except Exception as e:
        print(f"Error in Document Query module: {e}")

def run_audio_speech():
    try:
        response = measure_latency(dwani.Audio.speech, input="ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು , ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="wav")
        with open("output.wav", "wb") as f:
            f.write(response)
        print("Audio Speech: Output saved to output.wav")
    except Exception as e:
        print(f"Error in Audio Speech module: {e}")

def run_all_modules():
    print("\nRunning all modules...")
    run_chat()
    run_vision()
    run_asr()
    run_translate()
    run_doc_extract()
    run_doc_summarize()
    run_doc_query()
    run_audio_speech()

def display_menu():
    print("\ndwani.ai API Module Selector")
    print("1. Chat (default)")
    print("2. Vision")
    print("3. ASR")
    print("4. Translate")
    print("5. Document Extract")
    print("6. Document Summarize")
    print("7. Document Query")
    print("8. Audio Speech")
    print("9. Run All Modules")
    print("0. Exit")
    return input("Enter your choice (0-9, default is 1): ").strip()

def main():
    while True:
        choice = display_menu()

        # Default to Chat if no input or invalid input
        if not choice or choice not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            choice = "1"

        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            run_chat()
        elif choice == "2":
            run_vision()
        elif choice == "3":
            run_asr()
        elif choice == "4":
            run_translate()
        elif choice == "5":
            run_doc_extract()
        elif choice == "6":
            run_doc_summarize()
        elif choice == "7":
            run_doc_query()
        elif choice == "8":
            run_audio_speech()
        elif choice == "9":
            run_all_modules()

if __name__ == "__main__":
    main()
