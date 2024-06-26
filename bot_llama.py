import os
from groq import Groq
import streamlit as st
st.set_page_config(
    page_title="Hungarian to English and English to Hungarian Chatbot", 
    page_icon="💬")
groq_api_key=os.environ.get("GROQ_API_KEY")
st.title("Hungarian to English and English to Hungarian Chatbot 🤖")
st.markdown(
    """
<style>
    
    .st-emotion-cache-janbn0 {
        flex-direction: row-reverse;
        text-align: right;
    }

    .stChatMessage.st-emotion-cache-1c7y2kd.eeusbqq4[data-testid="stChatMessage"]{
        flex-direction: row-reverse;
        text-align: right;
    
    }
    
    .st-emotion-cache-jmw8un {
        background-color: rgb(9, 171, 59);
        
    }
    
    .st-emotion-cache-4zpzjl{
        background-color: rgb(252, 175, 69);
        
    }

    [data-testid="stToolbar"].st-emotion-cache-15ecox0.ezrtsby0 {
    display: none;
    
    }

</style>
""",
    unsafe_allow_html=True,
)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "You are a Hungarian to English and English to Hungarian translator chatbot. Your task is only to translate the text from English to Hungarian and vice versa. You should not answer any other questions. You are striclty a translator and nothing else"}]
st.chat_message("assistant").write("Hungarian to English and English to Hungarian Chatbot. How can I assist you today?")
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not groq_api_key:
        st.info("Please add your Groq Cloud API key to continue.")
        st.stop()

    client = Groq(api_key=groq_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="llama3-70b-8192", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
