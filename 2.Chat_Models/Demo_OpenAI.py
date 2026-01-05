#Closed Source Model, API key
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')       #In LLM it was llm and not model
#we can get creative response by adding temperature.
#model=ChatOpenAI(model='gpt-4',temperature=0)  
#Another parameter is max_completion_tokens.
#max_completion_tokens=10, To limit down tokens as there is cost associated with each.

result=model.invoke("What is the capital of India?")

print(result.content)             #We fetch result.content and not just result
