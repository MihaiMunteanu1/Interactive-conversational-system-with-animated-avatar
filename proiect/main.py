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


def generateImage(prompt, output_path="avatar.png"):
    client = OpenAIClient()

    image_data = client.generate_image(prompt)

    if image_data:
        with open(output_path, "wb") as f:
            f.write(image_data)
        print(f"Avatar generated and saved to {output_path}")
        return output_path
    else:
        print("Failed to generate avatar image")
        return None

def main():
    assistant = OpenAIClient()
    speech_engine = SpeechEngine()

    print("Press 'Enter' to begin the chat!")
    print("Say 'exit', 'quit' or 'stop' to close the chat.")
    print("Say 'generate image [description]' to create a new avatar.")


    try:
        while True:
            input("Press Enter to speak...")

            audio_file = record_audio(RECORDING_DURATION, TEMP_AUDIO_FILE)
            if not audio_file:
                continue

            user_input = speech_engine.speech_to_text(audio_file)
            if not user_input:
                print("Could not understand audio. Please try again.")
                clear_file(audio_file)
                continue

            print(f"You: {user_input}")

            if user_input.lower().startswith("generate image"):
                prompt = user_input[len("generate image"):].strip()
                if prompt:
                    print(f"Generating image with prompt: {prompt}")
                    new_image_path = generateImage(prompt)
                    if new_image_path:
                        image_path = new_image_path
                        print(f"Using new avatar: {image_path}")
                        response = "I've generated a new avatar based on your description."
                    else:
                        response = "I couldn't generate an image with that description."
                else:
                    response = "Please provide a description for the image."

                speech_engine.text_to_speech(response)
                print(f"Assistant: {response}")
                continue

            if user_input.lower() in ['exit', 'quit', 'stop']:
                print("Assistant: Goodbye!")
                speech_engine.text_to_speech("Goodbye!")
                clear_file(audio_file)
                clear_file(audio_path)
                break



            response = assistant.ask(user_input, instructions)
            print(f"Assistant: {response}")
            speech_engine.text_to_speech(response)

            #Pentru SadTalker:
            # os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
            # subprocess.run([
            #     "python", "../SadTalker/inference.py",
            #     "--source_image", image_path,
            #     "--driven_audio", audio_path
            # ], check=True)
            #

            clear_file(audio_file)
            clear_file(audio_path)

    except KeyboardInterrupt:
        print("\n[INFO] Session ended by user")
    finally:
        clear_file(TEMP_AUDIO_FILE)
        print("[INFO] System shutdown complete")

if __name__ == "__main__":
    main()
