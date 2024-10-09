from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
# from langchain.prompts import ChatPromptTemplate

# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
_ = load_dotenv(find_dotenv()) # read local .env file
chat = ChatOpenAI(temperature=0.0)
print(chat)
