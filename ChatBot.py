from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.1",
    task="text-generation",
    # max_new_tokens=64
)

model=ChatHuggingFace(llm=llm)

while True:
    user_input=input('You: ')
    if user_input == 'exit':
        break
    result=model.invoke(user_input)
    print("Parw_AI says :",result.content)
