#Open Source Model, API key
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.1",
    task="text-generation",
    # max_new_tokens=64
)

model=ChatHuggingFace(llm=llm)

response=model.invoke("Who is known as Captain Cool in Indian cricket?")

print(response.content)
