import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")


def run_translate():
    try:
        result = dwani.Translate.run_translate(sentences="hi, i am gaganyatri", src_lang="english", tgt_lang="kannada")

        print("Translate Result:", result)

        file_name = "shrimad_bhagavatam_english.txt"
        # Open the file in read mode
        with open(file_name, 'r') as file:
            file_content = file.read()

        # Now file_content holds the entire content of the file as a string
        print(file_content)

        result = dwani.Translate.run_translate(sentences=file_content, src_lang="english", tgt_lang="kannada")

        print(result)



    except Exception as e:
        print(f"Error in ASR module: {e}")


run_translate()
'''
def display_menu():
    print("\ndwani.ai Translate API Module Selector")
    print("1. Translate")
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
            run_translate()

if __name__ == "__main__":
    main()

'''