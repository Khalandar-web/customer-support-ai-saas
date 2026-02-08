from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Health check
@app.get("/")
def health_check():
    return {"status": "Backend is running"}

# Request body model
class ChatMessage(BaseModel):
    message: str

# Chat endpoint
@app.post("/chat")
def chat(chat: ChatMessage):
    ai_service_url = "http://ai:8001/generate"

    response = requests.post(
        ai_service_url,
        json={"message": chat.message}
    )

    ai_reply = response.json().get("reply")

    return {
        "user_message": chat.message,
        "ai_reply": ai_reply
    }
