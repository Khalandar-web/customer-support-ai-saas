from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# CORS (frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Read API key from ENV
AI_API_KEY = os.getenv("AI_API_KEY")

@app.get("/")
def health_check():
    return {
        "status": "Backend is running",
        "api_key_loaded": AI_API_KEY is not None
    }

@app.post("/chat")
def chat(payload: dict):
    # TEMP response using ENV
    return {
        "reply": f"API key received ✅ ({AI_API_KEY}) | Message: {payload.get('message')}"
    }
