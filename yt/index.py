import os
import openai
from dotenv import load_dotenv, find_dotenv
# from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseOutputParser
# from langchain.schema.messages import HumanMessage, SystemMessage
_ = load_dotenv(find_dotenv()) # read local .env file
# key="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"
chat = ChatOpenAI()
response = chat.invoke("List the seven wonders of the world.")
print(response)

# try:
#     response = llm("Hello!")
# except openai.error.OpenAIError as e:
#     print(f"An error occurred: {e}")
# print(llm("explain LLM in single sentence."))
