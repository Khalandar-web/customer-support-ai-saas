import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AI_API_KEY = os.getenv("AI_API_KEY")

@app.get("/")
def health():
    return {"status": "Backend running"}

@app.post("/chat")
def chat(payload: dict):
    message = payload.get("message")

    # ❌ DO NOT PRINT OR RETURN API KEY
    # print(AI_API_KEY)  <-- NEVER DO THIS

    response = requests.post(
        "http://ai:8001/generate",
        json={
            "message": message,
            "api_key": AI_API_KEY
        }
    )

    return {
        "reply": response.json().get("reply")
    }
