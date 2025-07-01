import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")

# Function for each module
def run_chat():
    try:
        resp = dwani.Chat.create(prompt="Hello!", src_lang="english", tgt_lang="kannada")
        print("Chat Response: Eng-Kan- ", resp)

        resp = dwani.Chat.create(prompt="Hello!", src_lang="english", tgt_lang="english")
        print("Chat Response: Eng-Eng- ", resp)

        resp = dwani.Chat.create(prompt="Hello!", src_lang="english", tgt_lang="german")

        print("Chat Response: Eng-Ger- ", resp)
        resp = dwani.Chat.create(prompt="Hello!", src_lang="german", tgt_lang="german")
        
        print("Chat Response: Ger-Eng ", resp)
        resp = dwani.Chat.create(prompt="Hello!", src_lang="german", tgt_lang="english")
        
        print("Chat Response: Ger-Eng ", resp)
    except Exception as e:
        print(f"Error in Chat module: {e}")

def run_all_modules():
    print("\nRunning all modules...")
    run_chat()

def display_menu():
    print("\ndwani.ai Chat API Module Selector")
    print("1. Chat (default)")
    print("0. Exit")
    return input("Enter your choice (0-9, default is 1): ").strip()

def main():
    while True:
        choice = display_menu()

        # Default to Chat if no input or invalid input
        if not choice or choice not in {"0", "1"}:
            choice = "1"

        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            run_chat()

if __name__ == "__main__":
    main()