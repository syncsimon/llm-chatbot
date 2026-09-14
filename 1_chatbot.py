# import warnings
# warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
#importing llm model
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")
# making the UI for streamlit
st.title("Your personal AI Bot")
st.markdown("Can answer anything you ask within seconds")


if "messages" not in st.session_state: 
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input("hey simon! how are you")
if query:
    st.session_state.messages.append({"role":"user" , "content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content[0]["text"])
    st.session_state.messages.append({
        "role" : "ai" ,
        "content": res.content[0]["text"]
    })






