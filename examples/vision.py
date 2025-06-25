import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")


def run_vision():
    try:

        result = dwani.Vision.caption(
            file_path="image.png",
            query="Describe this image",
            src_lang="kannada",
            tgt_lang="kannada",
            model="gemma3"
        )
        print("Vision Response: Eng-Kan- ", result)
        result = dwani.Vision.caption(
            file_path="image.png",
            query="Describe this image",
            src_lang="english",
            tgt_lang="kannada",
            model="gemma3"
        )
        print("Vision Response: Eng-Kan- ", result)
        result = dwani.Vision.caption(
            file_path="image.png",
            query="Describe this image",
            src_lang="english",
            tgt_lang="english",
            model="gemma3"
        )
        print("Vision Response: Eng-Eng- ", result)

        result = dwani.Vision.caption(
            file_path="image.png",
            query="Describe this image",
            src_lang="english",
            tgt_lang="german",
            model="gemma3"
        )
        print("Vision Response: Eng-Ger- ", result)

        
        result = dwani.Vision.caption_direct(
            file_path="image.png",
            query="Describe this image",
            model="gemma3"
        )
        print("Vision Response: ", result)
        
    except Exception as e:
        print(f"Error in Vision module: {e}")


def display_menu():
    print("\ndwani API Module Selector")
    print("1. Vision")
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
            run_vision()

if __name__ == "__main__":
    main()