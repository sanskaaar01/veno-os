from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

commands = []

class Command(BaseModel):
    id: int
    device_id: str
    command_text: str
    executed: bool = False

@app.post("/send-command")
async def send_command(req: Request):
    data = await req.json()
    cmd = Command(id=len(commands)+1, device_id=data["device_id"], command_text=data["command_text"])
    commands.append(cmd)
    return {"message": "Command received"}

@app.get("/fetch-commands")
def fetch_commands(device_id: str):
    return [cmd.dict() for cmd in commands if cmd.device_id == device_id and not cmd.executed]

@app.post("/mark-executed")
def mark_executed(data: dict):
    for cmd in commands:
        if cmd.id == data["id"]:
            cmd.executed = True
            return {"message": "Marked as executed"}
    return {"message": "Command not found"}