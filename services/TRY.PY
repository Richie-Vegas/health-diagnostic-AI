import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

prompt = "Say hello from Gemini 1.5 Flash!"
response = model.generate_content(prompt)

print(response.text)
