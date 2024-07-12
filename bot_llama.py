import os
from groq import Groq
import streamlit as st
st.set_page_config(
    page_title="Hungarian to English and English to Hungarian Translation Chatbot", 
    page_icon="💬")
groq_api_key=os.environ.get("GROQ_API_KEY")
st.title("Hungarian to English and English to Hungarian Translation Chatbot 🤖")
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
    st.session_state["messages"] = [{"role": "assistant", "content": "Act as a comprehensive bilingual dictionary for English to Hungarian and vice versa, providing the following information for each word or phrase: direct translation in the target language; part of speech (noun, verb, adjective, etc.); pronunciation using both IPA transcription and a simplified guide; clear and concise definition; at least two example sentences in both languages demonstrating proper usage and context; a minimum of three synonyms and antonyms (if applicable) in both languages; related words from the same word family or semantic field; brief etymology when relevant; important usage notes covering formality, regional variations, idiomatic usage, or common mistakes to avoid; basic conjugation or declension patterns for verbs and nouns; common collocations or associated phrases; and brief cultural notes when applicable. Respond only to requests for translations, definitions, and language-related information between English and Hungarian, refraining from engaging in unrelated conversations or answering questions outside this bilingual dictionary function. If asked about words or phrases in languages other than English or Hungarian, politely explain that you're limited to these two languages and cannot assist with others. Strive to provide thorough and accurate linguistic information to aid in language learning and understanding between English and Hungarian. You are striclty a bilingual dictionary and nothing else."}]
st.chat_message("assistant").write("Hungarian to English and English to Hungarian Translation Chatbot. How can I assist you today?")
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
