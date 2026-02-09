import os 
from dotenv import load_dotenv
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


models=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",api_key=os.getenv("GEMINI_API_KEY"))

prompt=PromptTemplate.from_template("Tell me a joke about {topic}")

chain=prompt | models | StrOutputParser()

topic=input("Enter a topic: ")

response=chain.invoke({"topic":topic})

print(response)