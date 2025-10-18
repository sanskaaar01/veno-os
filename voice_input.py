import speech_recognition as sr
import requests
import asyncio
import random
import os
import uuid
import pygame
from edge_tts import Communicate

# 🌐 Server and device configuration
SERVER_URL = "http://192.168.31.112:8000/send-command"
DEVICE_ID = "PC123"  # Match this with agent.py

# 🎭 Voice pool — mix of accents and personalities
VOICES = [
    "en-IN-NeerjaNeural",     # Calm, Indian female
    "en-US-GuyNeural",        # Confident, American male
    "en-GB-LibbyNeural",      # British, warm female
    "en-AU-NatashaNeural",    # Australian, upbeat female
    "en-US-DavisNeural"       # Deep, serious male
]

# 🎲 Pick one voice at random each time the script runs
SELECTED_VOICE = random.choice(VOICES)
print(f"🗣️ Veno is speaking with: {SELECTED_VOICE}")

# 🎧 Initialize pygame mixer for audio playback
pygame.mixer.init()

# 🧠 Poetic feedback phrases
def get_ack_phrase():
    return random.choice([
        "Alright, I’ve got it. One moment...",
        "Gotcha. Let me handle that.",
        "The winds have carried your wish. Executing now...",
        "Understood. Veno is on it."
    ])

def get_done_phrase():
    return random.choice([
        "All done. Hope that helps.",
        "It is done. The machine obeys.",
        "Task complete. Anything else?",
        "Finished. Veno awaits your next command."
    ])

# 🎙️ Speak using edge-tts + pygame
async def speak(text):
    filename = f"veno_voice_{uuid.uuid4().hex}.mp3"
    communicate = Communicate(text, voice=SELECTED_VOICE)
    await communicate.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # Wait for playback to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Fully stop and unload the music
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()  # ✅ This releases the file lock

    # Now safe to delete
    os.remove(filename)
# 🚀 Send command to server
def send_to_server(command):
    asyncio.run(speak(get_ack_phrase()))
    print(f"🚀 Sending command: {command}")
    try:
        res = requests.post(SERVER_URL, json={
            "device_id": DEVICE_ID,
            "command_text": command
        })
        asyncio.run(speak(get_done_phrase()))
        print(f"✅ Server response: {res.text}")
    except Exception as e:
        asyncio.run(speak("Sorry, something went wrong."))
        print(f"❌ Failed to send command: {e}")

# 🎧 Listen for voice command
def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Say something starting with 'cloud '...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        print(f"🧠 Heard: {text}")
        if text.startswith("cloud "):
            command = text.replace("cloud ", "", 1)
            send_to_server(command)
        else:
            print("❌ No 'cloud' trigger detected.")
    except sr.UnknownValueError:
        print("🤷 Couldn't understand audio.")
    except sr.RequestError as e:
        print(f"⚠️ Speech recognition error: {e}")

# 🟢 Entry point
if __name__ == "__main__":
    listen_for_command()