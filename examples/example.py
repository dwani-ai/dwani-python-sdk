import time
import dwani
import os
import logging
from datetime import datetime

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")

# Create 'latency_logs' directory if it doesn't exist
log_dir = "latency_logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure the logging module to save logs in the 'latency_logs' directory
log_filename = os.path.join(log_dir, f"dwani_api_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(filename=log_filename, 
                    level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Function to measure latency of each call and log the info
def measure_latency(func, *args, **kwargs):
    start_time = time.time()  # Start timer
    try:
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # End timer
        latency = end_time - start_time  # Calculate latency
        logging.info(f"Latency for {func.__name__}: {latency:.4f} seconds")
        return result  # Return the result of the API call
    except Exception as e:
        logging.error(f"Error in {func.__name__}: {e}")
        raise  # Re-raise exception after logging

# Function for each module with latency measurement and logging
def run_chat():
    try:
        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada")
        logging.info("Chat Response: default/gemma3- " + str(resp))

        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada", model="qwen3")
        logging.info("Chat Response: qwen3- " + str(resp))

        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada", model="gemma3")
        logging.info("Chat Response: gemma3- " + str(resp))

        resp = measure_latency(dwani.Chat.create, prompt="Hello!", src_lang="english", tgt_lang="kannada", model="sarvam-m")
        logging.info("Chat Response: sarvam-m- " + str(resp))

        resp = measure_latency(dwani.Chat.direct, prompt="Hello!", model="qwen3")
        logging.info("Chat Response: qwen3/direct- " + str(resp))

        resp = measure_latency(dwani.Chat.direct, prompt="Hello!", model="gemma3")
        logging.info("Chat Response: gemma3/direct- " + str(resp))

        resp = measure_latency(dwani.Chat.direct, prompt="Hello!", model="sarvam-m")
        logging.info("Chat Response: sarvam-m/direct- " + str(resp))

    except Exception as e:
        logging.error(f"Error in Chat module: {e}")

def run_vision():
    try:
        result = measure_latency(dwani.Vision.caption, file_path="image.png", query="Describe this logo", src_lang="english", tgt_lang="kannada", model="gemma3")
        logging.info("Vision Response: gemma3- " + str(result))

        result = measure_latency(dwani.Vision.caption, file_path="image.png", query="Describe this logo", src_lang="english", tgt_lang="kannada", model="moondream")
        logging.info("Vision Response: moondream- " + str(result))

        result = measure_latency(dwani.Vision.caption_direct, file_path="image.png", query="Describe this logo", model="gemma3")
        logging.info("Vision Response: gemma3/direct- " + str(result))

        result = measure_latency(dwani.Vision.caption_direct, file_path="image.png", query="Describe this logo", model="moondream")
        logging.info("Vision Response: moondream/direct- " + str(result))

    except Exception as e:
        logging.error(f"Error in Vision module: {e}")

def run_asr():
    try:
        result = measure_latency(dwani.ASR.transcribe, file_path="kannada_sample.wav", language="kannada")
        logging.info("ASR Response: " + str(result))
    except Exception as e:
        logging.error(f"Error in ASR module: {e}")

def run_translate():
    try:
        # List of strings input
        resp = measure_latency(dwani.Translate.run_translate, sentences=["hi", "what is this?"], src_lang="english", tgt_lang="kannada")
        logging.info("Translate Response: " + str(resp))

        # Single string input
        resp = measure_latency(dwani.Translate.run_translate, sentences="hi, i am gaganyatri", src_lang="english", tgt_lang="kannada")
        logging.info("Translate Response: " + str(resp))

        # Open the file in read mode
        file_path = 'translation_large_content.txt'  # Replace with your file path

        with open(file_path, 'r') as file:
            text = file.read()

        resp = measure_latency(dwani.Translate.run_translate, sentences=text, src_lang="kannada", tgt_lang="english")
        logging.info("Translate Response: " + str(resp))

    except Exception as e:
        logging.error(f"Error in Translate module: {e}")

def run_doc_extract():
    try:
        result = measure_latency(dwani.Documents.run_extract, file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada")
        logging.info("Document Extract Response: " + str(result))

        result = measure_latency(dwani.Documents.run_extract, file_path="paper_1.pdf", page_number=1, src_lang="english", tgt_lang="kannada")
        logging.info("Document Extract Response: " + str(result))

    except Exception as e:
        logging.error(f"Error in Document Extract module: {e}")

def run_doc_summarize():
    try:
        result = measure_latency(dwani.Documents.summarize, file_path="dwani-workshop.pdf", page_number=1, src_lang="english", tgt_lang="kannada")
        logging.info("Document Summarize Response: default/gemma3- " + str(result))

    except Exception as e:
        logging.error(f"Error in Document Summarize module: {e}")

def run_doc_query():
    try:
        result = measure_latency(dwani.Documents.run_doc_query, file_path="dwani-workshop.pdf", prompt="list the key points", page_number=1, src_lang="english", tgt_lang="kannada", model="gemma3")
        logging.info("Document Query Response: gemma3- " + str(result))

        result = measure_latency(dwani.Documents.run_doc_query, file_path="paper_1.pdf", prompt="list the key points", page_number=1, src_lang="english", tgt_lang="kannada", model="gemma3")
        logging.info("Document Query Response: gemma3- " + str(result))

    except Exception as e:
        logging.error(f"Error in Document Query module: {e}")

def run_audio_speech():
    try:
        response = measure_latency(dwani.Audio.speech, input="ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು , ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="wav")
        with open("output.wav", "wb") as f:
            f.write(response)
        logging.info("Audio Speech: Output saved to output.wav")
    except Exception as e:
        logging.error(f"Error in Audio Speech module: {e}")

def run_all_modules():
    logging.info("\nRunning all modules...")
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
            logging.info("Exiting...")
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
