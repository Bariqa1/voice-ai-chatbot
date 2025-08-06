import sounddevice as sd
import vosk
import queue
import json
import pyttsx3
import cohere
import re
import threading

co = cohere.Client("YOUR_API_KEY")

model_path = r"models/vosk-model-small-en-us-0.15"
model = vosk.Model(model_path)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

device_info = sd.query_devices(None, 'input')
samplerate = int(device_info['default_samplerate'])

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_and_respond():
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 Speak now...")
        rec = vosk.KaldiRecognizer(model, samplerate)

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print("You said:", text)

                    clean_text = re.sub(r'[^a-zA-Z0-9 .,?!]', '', text)

                    response = co.chat(
                        model='command-nightly',
                        message=clean_text,
                        max_tokens=50
                    )
                    reply = response.text.strip()
                    print("Bot:", reply)

                    threading.Thread(target=speak, args=(reply,)).start()
recognize_and_respond() 
