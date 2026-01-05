from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('Research Tool')

user_input=st.text_input('Enter your prompt')   #Static Prompt

llm = HuggingFaceEndpoint(
    repo_id="MiniMaxAI/MiniMax-M2.1",
    task="text-generation",
    # max_new_tokens=64
)

model=ChatHuggingFace(llm=llm)

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)



