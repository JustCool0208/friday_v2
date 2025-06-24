import whisper 
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

model = whisper.load_model("base",device="cpu")

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎙️ Speak now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, fs, recording)
    print("✅ Recording saved.")


def transcribe(filename="input.wav"):
    result = model.transcribe(filename)
    return result["text"]
