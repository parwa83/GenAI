from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.1",
    task="text-generation",
    # max_new_tokens=64
)

model=ChatHuggingFace(llm=llm)

chat_history=[]

while True:
    user_input=input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result.content)
    print("Parw_AI says :",result.content)

print(chat_history)