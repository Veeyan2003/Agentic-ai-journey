import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


history=[]

summary=""

def summarise(chat_history):
    content=f"Summarise the following chat history in one sentence: {chat_history}" 
    response=client.models.generate_content(model="gemini-2.5-flash-lite",
    contents=content)
    return response.text

def chat_with_model(user_input):
    global history, summary
    full_instruction=f"System info:{summary}\n\n User Input:{user_input}"

    response=client.models.generate_content(model="gemini-2.5-flash-lite",
    config={"system_instruction":full_instruction},
    contents=user_input
    )
    history.append(f"User: {user_input}\nAI: {response.text}")

    if len(history)>5:
        print("summarising chat history...")
        summary=summarise(history)
        history=[]
        print(f"New summary: {summary}")

   
    return response.text


while True:
     user_input=input("You:")
     if user_input.lower() in ["exit","quit"]:
        break
     print(f"AI: {chat_with_model(user_input)}")

print("conversation ended")
