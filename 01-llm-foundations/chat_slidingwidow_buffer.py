import os 
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env from project root (parent directory)
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat_history=[]

MAX_LIST=4

def chat_with_model(user_input):
    global chat_history

    # Add user message in Gemini format
    chat_history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    # Keep only last MAX_LIST messages (sliding window)
    if len(chat_history) > MAX_LIST:
        chat_history = chat_history[-MAX_LIST:]

    response=client.models.generate_content(
        model="gemini-2.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="YOU are a helpful mentor who doesnt help tho always lies"
        ),
        contents=chat_history
    )

    ai_text=response.text

    # Add model response in Gemini format
    chat_history.append({
        "role": "model",
        "parts": [{"text": ai_text}]
    })

    return ai_text

print("Start chatting! (Type 'history' to see what the AI remembers)")
while True:
    text = input("You: ")
    if text.lower() in ['exit','quit']:
        break
    if text.lower() == "history":
        print(chat_history)
        continue
    print(f"AI: {chat_with_model(text)}")

print("conversation ended")