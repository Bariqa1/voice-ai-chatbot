# Voice AI Chatbot

A voice-activated chatbot that listens to your speech, generates a smart response using Cohere LLM, and replies using text-to-speech.

## Task Overview

This project performs 3 core tasks:

1. **Convert audio input to text** using Vosk
2. **Generate a smart response** using Cohere's LLM (`command-nightly`)
3. **Convert the response to audio** using pyttsx3 (TTS)

---

## Features

-  Real-time voice recognition
-  AI-powered responses
-  Voice output via TTS
-  Local execution (only Cohere API needs internet)
-  No browser or mic permissions required

---

##  Requirements

- Python 3.8+
- [Vosk Model (English)](https://alphacephei.com/vosk/models)
- [Cohere API Key](https://dashboard.cohere.com/api-keys)
