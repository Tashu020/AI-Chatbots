from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro Model
model = genai.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    response.resolve()
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Arnav - The All-Knowing")

# Initialize chat history in session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit and input_text:
    response = get_gemini_response(input_text)

    st.session_state['chat_history'].append(("You", input_text))
    st.session_state['chat_history'].append(("Bot", response))

    st.subheader("The response is")
    st.write(response)

st.subheader("The Chat history is:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
