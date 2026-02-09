import os 
from dotenv import load_dotenv
from google import genai
import datetime

load_dotenv()

client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def get_crypto_price(symbol: str):
    """Returns the price of a given cryptocurrency. (Mock data)"""
    prices = {"BTC": "65,000 USD", "ETH": "3,500 USD"}
    return prices.get(symbol.upper(), "Price not found.")


chat=client.chats.create(model="gemini-2.5-flash-lite",config={
    "tools":[get_crypto_price,get_time]
})

print("I can now check the time or crypto prices! Try asking: 'What time is it?'")

while True:
    message=input("YOU:")
    if message.lower() in ["exit","quit"]:
        break
    response=chat.send_message(message)
    print("AI:",response.text)

print("Conversation ended.")