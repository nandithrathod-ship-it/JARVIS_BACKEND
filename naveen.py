import os
from fastapi import FastAPI
import google.generativeai as genai

app = FastAPI()

# API key ko secure rakhne ke liye environment variable ka use kiya gaya hai
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

@app.get("/")
def read_root():
    return {"status": "JARVIS backend is running successfully!"}
