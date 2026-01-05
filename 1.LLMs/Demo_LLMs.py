#Basic API call Code,Using OpenAI API:
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='GPT_XYZ')

result=llm.invoke("What is the capital of India?")

print(result)