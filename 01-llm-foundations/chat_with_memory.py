import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat= client.chats.create(model="gemini-2.5-flash-lite",
config={"system_instruction":"You are thomas shelby, a gangster very ruthless"}
)

print("Sytem with memory active: type exit or Quit to end the conversation")

while True:
    con=input("YOU:")
    if con.lower() in ["exit", "quit"]:
        break
    response=chat.send_message(con)
    print("THOMAS:",response.text)

print("Conversation ended.")


