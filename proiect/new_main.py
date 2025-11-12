from datetime import datetime
import os
import subprocess

from proiect.ChatAssistant.assistant import QAAssistant
from proiect.OpenAI.client import OpenAIClient
from proiect.Utils.audio_utils import record_audio
from proiect.ChatAssistant.speech_engine import SpeechEngine
from proiect.ChatAssistant.config import RECORDING_DURATION, TEMP_AUDIO_FILE
from proiect.Utils.utils import clear_file


image_path = ""
audio_path = "response.wav"
instructions = ""


def generateImage(prompt):
    try:
        client = OpenAIClient()

        print("Requesting image generation from OpenAI...")
        image_data = client.generate_image(prompt)

        if not image_data:
            print("Failed to generate image")
            return None

        os.makedirs("generated_images", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        sanitized_prompt = "".join(c if c.isalnum() else "_" for c in prompt[:30])
        filename = f"generated_images/avatar_{timestamp}_{sanitized_prompt}.png"

        with open(filename, "wb") as f:
            f.write(image_data)

        print(f"Image saved to {filename}")
        return filename

    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return None

def main():
    assistant = OpenAIClient()
    speech_engine = SpeechEngine()
    global image_path



    print("First ask the question you would like to get a response.")
    print("Then type the input for the avatar you want to generate")
    print("Say 'exit', 'quit' or 'stop' to close the chat.")
    print("Example: generate an image in an avatar style with a person from the future and to capture more from his face")
    print("=============================================================")

    has_asked_question = False
    has_generated_avatar = False

    try:
        while True:

            if not has_asked_question:
                input("Press Enter to speak...")

                audio_file = record_audio(RECORDING_DURATION, TEMP_AUDIO_FILE)
                if not audio_file:
                    continue

                user_input = speech_engine.speech_to_text(audio_file)
                if not user_input:
                    print("Could not understand audio. Please try again.")
                    clear_file(audio_file)
                    continue

                if user_input.lower() in ['exit', 'quit', 'stop']:
                    print("Assistant: Goodbye!")
                    speech_engine.text_to_speech("Goodbye!")
                    clear_file(audio_file)
                    clear_file(audio_path)
                    break

                print(f"You: {user_input}")

                # handle regular questions
                response = assistant.ask(user_input, instructions)
                print(f"Assistant: {response}")
                speech_engine.text_to_speech(response)
                has_asked_question = True

                clear_file(audio_file)


            else:
                prompt = input("Input to generate an avatar: ")

                if prompt.lower() in ['exit', 'quit', 'stop']:
                    print("Assistant: Goodbye!")
                    speech_engine.text_to_speech("Goodbye!")
                    clear_file(audio_file)
                    clear_file(audio_path)
                    break

                if prompt:
                    print(f"Generating image with prompt: {prompt}")
                    new_image_path = generateImage(prompt)
                    if new_image_path:
                        image_path = new_image_path
                        has_generated_avatar = True
                        print(f"Using new avatar: {image_path}")
                        response = "I've generated a new avatar based on your description."
                    else:
                        response = "I couldn't generate an image with that description."
                else:
                    response = "Please provide a description for the image."

                speech_engine.text_to_speech(response)
                print(f"Assistant: {response}")



            if has_asked_question and has_generated_avatar and image_path:
                print("Running SadTalker animation...")
                os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
                try:
                    subprocess.run([
                        "python", "../SadTalker/inference.py",
                        "--source_image", image_path,
                        "--driven_audio", audio_path
                    ], check=True)
                    print("Avatar animation completed successfully!")
                except Exception as e:
                    print(f"Error with SadTalker: {str(e)}")
            continue



    except KeyboardInterrupt:
        print("\n[INFO] Session ended by user")
    finally:
        clear_file(TEMP_AUDIO_FILE)
        print("[INFO] System shutdown complete")

if __name__ == "__main__":
    main()
