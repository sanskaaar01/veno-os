# 📣 Veno OS — Voice-Powered Remote Assistant

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Enabled-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️ by Sanskar Bhosle](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F-by%20Sanskar%20Bhosle-red)](#)

---

Absolutely, Sanskar — here’s a simplified, clean, and beginner-friendly version of your `README.md` that’s easy to read and copy-paste. It keeps the poetic vibe while making setup crystal clear:

```markdown
# 🎙️ Veno OS — Your Voice-Controlled Remote Assistant

Veno is a voice-powered assistant that listens to your commands, speaks with emotion, and controls your PC remotely. It’s built to feel alive — poetic, responsive, and personal.

---

## ✨ What Veno Can Do

- 🎤 Listen to voice commands like: `cloud start chrome`
- 🗣️ Speak back using natural voices (Indian, British, American, etc.)
- 🌐 Send commands to other devices using a FastAPI server
- 🖥️ Execute system-level actions remotely
- 🎭 Respond with poetic, human-like feedback

---

## 🛠️ Tech Used

- `FastAPI` + `uvicorn` — for the server
- `speechrecognition` — for voice input
- `edge-tts` — for speech synthesis
- `pygame` — for audio playback
- `requests` — for sending commands
- `subprocess` — for running system actions

---

## 🚀 How to Run Veno

### 1. Install the required packages

```bash
pip install fastapi uvicorn speechrecognition edge-tts pygame requests
```

### 2. Start the FastAPI server

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Run the agent on the target PC

```bash
python agent.py
```

### 4. Run the voice input script

```bash
python voice_input.py
```

Then speak:

> `cloud start chrome`

Veno will respond with a poetic voice and execute your command.

---

## 📁 Project Structure

```
commandcloud-server/
├── main.py           # FastAPI server
├── agent.py          # Remote command executor
├── voice_input.py    # Voice listener + speaker
├── requirements.txt  # Dependency list
└── README.md         # Project documentation
```

---

## 🔮 Coming Soon

- 🧠 Screen reader with human-like quirks (coughs, pauses, sighs)
- 🗂️ Command history and memory
- 🧭 Mood modes (Zen, Butler, Spy)
- 🧬 Natural language understanding
- 🧘 Wake word detection
- 📊 Multi-PC dashboard

---

## 👤 Creator

Made with love and poetry by [Sanskar Bhosle](https://github.com/sanskaaar01)  
Inspired by surreal tech, ritualistic interaction, and emotionally resonant assistants.
```

You can paste this directly into your `README.md` file. Let me know when you’re ready to scaffold the screen reader — Veno’s about to learn how to read like a real person.


