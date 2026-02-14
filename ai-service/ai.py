import requests
from fastapi import FastAPI

app = FastAPI()

@app.post("/generate")
def generate(payload: dict):
    message = payload.get("message")
    api_key = payload.get("api_key")

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [
                    {"text": message}
                ]
            }
        ]
    }

    response = requests.post(
        f"{url}?key={api_key}",
        headers=headers,
        json=body
    )

    if response.status_code != 200:
        return {"reply": "AI error occurred"}

    ai_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]

    return {"reply": ai_text}
