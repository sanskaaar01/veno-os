import requests
import time
import subprocess

DEVICE_ID = "PC123"  # Match this with the device_id used in voice_input.py
SERVER_URL = "http://192.168.31.112:8000"

def fetch_commands():
    try:
        response = requests.get(f"{SERVER_URL}/fetch-commands", params={"device_id": DEVICE_ID})
        return response.json()
    except Exception as e:
        print(f"❌ Error fetching commands: {e}")
        return []

def mark_executed(command_id):
    try:
        requests.post(f"{SERVER_URL}/mark-executed", json={"id": command_id})
        print(f"✅ Marked command {command_id} as executed")
    except Exception as e:
        print(f"⚠️ Error marking executed: {e}")

def run_loop():
    print(f"🖥️ Veno agent started for device: {DEVICE_ID}")
    while True:
        commands = fetch_commands()
        for cmd in commands:
            print(f"🧠 Executing: {cmd['command_text']}")
            try:
                subprocess.Popen(cmd["command_text"], shell=True)
                mark_executed(cmd["id"])
            except Exception as e:
                print(f"❌ Execution failed: {e}")
        time.sleep(3)

if __name__ == "__main__":
    run_loop()