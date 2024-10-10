import os
import openai
from dotenv import load_dotenv, find_dotenv
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseOutputParser
# from langchain.schema.messages import HumanMessage, SystemMessage
_ = load_dotenv(find_dotenv()) # read local .env file
chat = ChatOpenAI()
response = chat.invoke("List the seven wonders of the world.")
print(response)

# try:
#     response = llm("Hello!")
# except openai.error.OpenAIError as e:
#     print(f"An error occurred: {e}")
# print(llm("explain LLM in single sentence."))
