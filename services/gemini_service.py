# multi_agent_diagnosis/app/services/gemini_service.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini with your API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_diagnosis(message: str) -> str:
    prompt = f"""
    You are a multi-specialty medical AI. 
    A patient reports these symptoms: {message}
    
    Give a diagnosis hypothesis and suggest possible conditions. Be concise and safe.
    """

    response = genai.generate_text(
        model="gemini-pro",
        prompt=prompt,
        temperature=0.2,
    )

    return response.text
