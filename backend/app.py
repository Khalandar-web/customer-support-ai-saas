from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# ✅ FINAL CORS CONFIG (frontend on 8080 allowed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://127.0.0.1:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "Backend is running"}

@app.post("/chat")
def chat(payload: dict):
    response = requests.post(
        "http://ai:8001/generate",
        json=payload
    )
    return response.json()
