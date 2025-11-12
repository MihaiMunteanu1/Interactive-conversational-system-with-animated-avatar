import sounddevice as sd
from scipy.io.wavfile import write
from proiect.ChatAssistant.config import SAMPLE_RATE, TEMP_AUDIO_FILE
from proiect.Utils.utils import handle_error

def record_audio(duration, filename=TEMP_AUDIO_FILE):
    try:
        print("Listening...")
        audio = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype='int16'
        )
        sd.wait()
        write(filename, SAMPLE_RATE, audio)
        return filename
    except Exception as e:
        handle_error("Recording failed", e)
        return None