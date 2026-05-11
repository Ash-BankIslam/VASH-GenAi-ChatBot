import streamlit as st
from google import genai

st.title("💬 Gemini Chatbot")

# Initialize client once
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=st.secrets["api_keys"]["gemini"])

MODEL_NAME = "models/gemini-flash-latest"

# Initialize chat once
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model=MODEL_NAME)

# Keep our own history list
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Send message to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Save both user and Gemini messages
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Gemini", response.text))

    # Display Gemini’s reply
    st.markdown(f"**Gemini:** {response.text}")

# Show conversation history
with st.expander("Conversation history"):
    for role, text in st.session_state.history:
        st.write(f"**{role}:** {text}")
