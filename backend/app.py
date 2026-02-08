from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# ✅ CORS (OK for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ READ AI SERVICE URL FROM ENV
AI_SERVICE_URL = os.getenv(
    "AI_SERVICE_URL",
    "http://localhost:8001/generate"  # fallback for local testing
)

@app.get("/")
def health_check():
    return {"status": "Backend is running"}

@app.post("/chat")
def chat(payload: dict):
    response = requests.post(
        AI_SERVICE_URL,
        json=payload
    )
    return response.json()
