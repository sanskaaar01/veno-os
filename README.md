# 📣 Veno OS — Voice-Powered Remote Assistant

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Enabled-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️ by Sanskar Bhosle](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F-by%20Sanskar%20Bhosle-red)](#)

---

**Veno** is a poetic, voice-controlled remote agent that listens, speaks, and executes system-level commands across devices.  
Built with **FastAPI**, **edge-tts**, and **pygame**, Veno blends natural speech with remote automation — making your machine feel alive.

---

## 🧠 Features

- 🎙️ **Voice Input** — Say `"cloud start chrome"` and Veno obeys  
- 🗣️ **Natural Speech** — Uses `edge-tts` with randomized voices (Indian, British, American, etc.)  
- 🎭 **Poetic Feedback** — Responds with human-like phrases and emotional tone  
- 🌐 **FastAPI Server** — Routes commands to connected agents  
- 🖥️ **Remote Agent** — Executes commands on target PC  
- 🔁 **Real-Time Execution** — Voice → Server → Agent → Action  

---

## 🛠️ Tech Stack

| Layer              | Tech Used                                      |
|--------------------|------------------------------------------------|
| Voice Input        | `speechrecognition`, `edge-tts`, `pygame`      |
| Server             | `FastAPI`, `uvicorn`                           |
| Agent              | `subprocess`, `requests`                       |
| Playback           | `pygame.mixer`                                 |
| OCR (coming soon)  | `pytesseract`, `pyautogui`                     |

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install fastapi uvicorn speechrecognition edge-tts pygame requests


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


