from fastapi import FastAPI, Request
from app.services.gemini_service import get_gemini_diagnosis

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("user_message", "")
    
    # Get diagnosis from Gemini
    diagnosis = get_gemini_diagnosis(user_message)
    
    return {"reply": diagnosis}
