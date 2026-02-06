import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env from project root (parent directory)
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

# Ensure your .env key matches exactly: GEMINI_API_KEY
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please check your .env file.")

client = genai.Client(api_key=api_key)

def generate_response(user_input, system_behavior, temp=0.7):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=system_behavior,
            temperature=temp,
            response_mime_type="application/json"
        ),
        contents=user_input
    )
    return response.candidates[0].content.parts[0].text

user_p = input("User: ")
sys_p = input("System Persona: ")

# Let's try it with a high temperature!
print(generate_response(user_p, sys_p, temp=1.5))

