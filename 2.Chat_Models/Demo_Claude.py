#Closed Source Model, API key
from lanchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model='claude:XYZ')

result=model.invoke("What is the capital of India?")

print(result.content)


#Here we see the beauty of LANGCHAIN,with just minimal 
# changes we can use any ChatModel