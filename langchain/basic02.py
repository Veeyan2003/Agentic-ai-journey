"""
Tiny LangChain example #1

Goal: show the absolute basics of how LangChain represents prompts,
and how a chat model is created. We will keep this file very small
and build on it over time.
"""

import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


# 1) Load environment variables from the .env file so we can get the API key.
load_dotenv()


# 2) Create a chat model that talks to Gemini via LangChain.
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)


# 3) Define a simple chat prompt template.
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a friendly assistant who explains things simply."),
        ("user", "{question}"),
    ]
)


# 4) Combine the prompt and the model into a simple "chain".
chain = prompt | model


if __name__ == "__main__":
    user_question = input("Ask me anything: ")
    result = chain.invoke({"question": user_question})
    print("Model:", result.content)

