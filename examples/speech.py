import dwani
import os

# Set API key and base URL
dwani.api_key = os.getenv("DWANI_API_KEY")
dwani.api_base = os.getenv("DWANI_API_BASE_URL")

def run_audio_speech():
    try:
        response = dwani.Audio.speech(input="ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="wav")
        with open("output.wav", "wb") as f:
            f.write(response)
        print("Audio Speech: Output saved to output.wav")

        response = dwani.Audio.speech(input="ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ಯಾವುದು", response_format="wav", language="kannada")
        with open("output_kannada.wav", "wb") as f:
            f.write(response)
        print("Audio Speech: Output saved to output_kannada.wav")


        response = dwani.Audio.speech(input="What is your name?", response_format="wav", language="english")
        with open("output_english.wav", "wb") as f:
            f.write(response)
        print("Audio Speech: Output saved to output_english.wav")


        response = dwani.Audio.speech(input="was ist das?", response_format="wav", language="german")
        with open("output_german.wav", "wb") as f:
            f.write(response)
        print("Audio Speech: Output saved to output_german.wav")
    except Exception as e:
        print(f"Error in Audio Speech module: {e}")

def display_menu():
    print("\ndwani.ai TTS API Module Selector")
    print("1. TTS Speech")
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
            run_audio_speech()

if __name__ == "__main__":
    main()