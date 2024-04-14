import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import os


KEY = os.getenv("OPENAI_API_KEY")


st.set_page_config(page_title='Conversational QA')
st.header("Hey Let's chat")


chat=ChatOpenAI(openai_api_key=KEY,temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]

def open_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    return answer.content


input=st.text_input("Input: ",key="input")
response=open_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)



