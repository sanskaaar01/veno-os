import requests
import time
import os

DEVICE_ID = "my-pc-001"
SERVER_URL = "http://127.0.0.1:8000"

def parse_command(text):
    text = text.lower().strip()

    # Browser and web
    if "open chrome" in text:
        return "start chrome"
    elif "open youtube" in text:
        return "start https://youtube.com"
    elif "open gmail" in text:
        return "start https://mail.google.com"
    elif "open whatsapp" in text:
        return "start https://web.whatsapp.com"
    elif "launch browser" in text:
        return "start chrome"

    # System apps
    elif "open notepad" in text:
        return "start notepad"
    elif "open calculator" in text:
        return "start calc"
    elif "open command prompt" in text or "open cmd" in text:
        return "start cmd"
    elif "open settings" in text:
        return "start ms-settings:"

    # System actions
    elif "shutdown pc" in text:
        return "shutdown /s /t 0"
    elif "restart pc" in text:
        return "shutdown /r /t 0"
    elif "lock pc" in text:
        return "rundll32.exe user32.dll,LockWorkStation"

    # Media
    elif "play music" in text:
        return "start wmplayer"
    elif "open pictures" in text:
        return "start shell:My Pictures"
    elif "open downloads" in text:
        return "start shell:Downloads"

    # Echo
    elif text.startswith("echo "):
        return text

    # Fallback
    else:
        return "start " + text

def fetch_commands():
    try:
        print("🔄 Fetching commands from server...")
        response = requests.get(f"{SERVER_URL}/fetch-commands", params={"device_id": DEVICE_ID})
        print("📦 Raw response:", response.text)
        response.raise_for_status()
        commands = response.json()
        print(f"✅ Received {len(commands)} command(s).")
        return commands
    except Exception as e:
        print(f"❌ Error fetching commands: {e}")
        return []

def mark_executed(cmd_id):
    try:
        response = requests.post(f"{SERVER_URL}/mark-executed", json={"id": cmd_id})
        response.raise_for_status()
        print(f"✅ Marked command {cmd_id} as executed.")
    except Exception as e:
        print(f"❌ Error marking command {cmd_id} as executed: {e}")

def run():
    print("🚀 Agent started. Polling every 10 seconds...\n")
    while True:
        commands = fetch_commands()
        for cmd in commands:
            parsed = parse_command(cmd["command_text"])
            print(f"⚡ Executing: {parsed}")
            os.system(parsed)
            mark_executed(cmd["id"])
        time.sleep(10)

if __name__ == "__main__":
    run()