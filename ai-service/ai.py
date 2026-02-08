from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AIRequest(BaseModel):
    message: str

@app.get("/")
def health():
    return {"status": "AI service is running"}

@app.post("/generate")
def generate_reply(request: AIRequest):
    return {
        "reply": f"AI Support Reply: We received your message -> '{request.message}'"
    }
