import numpy as np
import whisper
import pyttsx3
from proiect.ChatAssistant.config import WHISPER_MODEL
from proiect.Utils.utils import handle_error


class SpeechEngine:
    def __init__(self):
        self.whisper_model = whisper.load_model(WHISPER_MODEL)
        self.tts_engine = self.init_tts()

    @staticmethod
    def init_tts():
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            return engine
        except Exception as e:
            handle_error("TTS initialization failed", e)
            return None

    def speech_to_text(self, filename):
        try:
            from scipy.io import wavfile
            _, audio = wavfile.read(filename)

            audio = audio.astype(np.float32) / np.iinfo(audio.dtype).max

            result = self.whisper_model.transcribe(audio)
            return result["text"].strip()
        except Exception as e:
            handle_error("Speech recognition failed", e)
            return ""

    def text_to_speech(self, text, filename=None):
        if self.tts_engine and text:
            try:
                if filename:
                    self.tts_engine.save_to_file(text, filename)
                    self.tts_engine.runAndWait()
                    return filename
                else:
                    self.tts_engine.say(text)
                    self.tts_engine.runAndWait()
            except Exception as e:
                handle_error("Speech synthesis failed", e)
