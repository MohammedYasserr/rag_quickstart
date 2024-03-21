from langchain_community import output_parsers
from langchain_core import prompts
from pydantic import BaseModel
from langchain_community import vectorstores
from langchain_core import embeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv



# using the apikey
API_KEY = load_dotenv(dotenv_path=('C:/Users/Yasser/Downloads/rag_quickstart/.env'))

# Inializing an instance
llm = ChatOpenAI(model='gpt-3.5-turbo-1106' , temperature=0.5 , api_key=API_KEY)
