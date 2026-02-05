import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Ensure your .env key matches exactly: GEMINI_API_KEY
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(user_input, system_behavior, temp=0.7):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_behavior,
            temperature=temp,
        ),
        contents=user_input
    )
    return response.text

user_p = input("User: ")
sys_p = input("System Persona: ")

# Let's try it with a high temperature!
print(generate_response(user_p, sys_p, temp=1.5))

