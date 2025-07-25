import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")

def run_vision():
    try:
        result = dwani.Chat.direct(
            prompt="Hi, I am gaganyatri",
            model="gemma3"
        )
        
        print(result)
        
        result = dwani.Vision.caption(
            file_path="image.png",
            query="Describe this image",
            src_lang="english",
            tgt_lang="german",
            model="gemma3"
        )
        print(result)
        
        result = dwani.Vision.caption_direct(
            file_path="image.png",
            query="Describe this image",
            src_lang="english",
            tgt_lang="german",
            model="gemma3"
        )

    except Exception as e:
        print(f"Error in Vision module: {e}")



def run_all_modules():
    print("\nRunning all modules...")
    run_vision()

def display_menu():
    print("\nDhwani API Module Selector")
    print("2. Vision")
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
        elif choice == "2":
            run_vision()
        elif choice == "9":
            run_all_modules()

if __name__ == "__main__":
    main()