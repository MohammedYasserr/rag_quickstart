from langchain_community import output_parsers
from langchain_core import prompts
from pydantic import BaseModel
from langchain_community import vectorstores
from langchain_core import embeddings
from langchain_openai import ChatOpenAI



# Inializing an instance
llm = ChatOpenAI(model='gpt-3.5-turbo-1106' , temperature=0.5)

# Todo, solve the dotenv installing problem