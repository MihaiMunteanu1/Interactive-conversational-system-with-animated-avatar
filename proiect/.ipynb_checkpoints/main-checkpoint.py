from proiect.ChatAssistant.assistant import QAAssistant
from proiect.Utils.audio_utils import record_audio
from proiect.ChatAssistant.speech_engine import SpeechEngine
from proiect.ChatAssistant.config import RECORDING_DURATION, TEMP_AUDIO_FILE
from proiect.Utils.utils import clear_file


def main():
    assistant = QAAssistant()
    speech_engine = SpeechEngine()

    print("Press 'Enter' to begin the chat!")
    print("Say 'exit', 'quit' or 'stop' to close the chat.")

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

            if user_input.lower() in ['exit', 'quit', 'stop']:
                print("Assistant: Goodbye!")
                speech_engine.text_to_speech("Goodbye!")
                clear_file(audio_file)
                break

            response = assistant.ask(user_input)
            print(f"Assistant: {response}")

            speech_engine.text_to_speech(response)

            clear_file(audio_file)

    except KeyboardInterrupt:
        print("\n[INFO] Session ended by user")
    finally:
        clear_file(TEMP_AUDIO_FILE)
        print("[INFO] System shutdown complete")

if __name__ == "__main__":
    main()