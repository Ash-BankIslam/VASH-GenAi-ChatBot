import streamlit as st
from google import genai   # use google-genai, not google.generativeai

st.title("💬 Gemini Chatbot")

# Initialize client once
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=st.secrets["api_keys"]["gemini"])

MODEL_NAME = "models/gemini-flash-latest"  # safe alias for latest Flash model

# Initialize chat once
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model=MODEL_NAME)

# Keep our own history list (user + Gemini turns)
if "history" not in st.session_state:
    st.session_state.history = []

# Chat-style input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Send message to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Save both user and Gemini messages
    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("assistant", response.text))

# Render conversation in chat bubbles
for role, text in st.session_state.history:
    st.chat_message(role).write(text)

# Optional: reset button like Gemini web "New chat"
if st.button("Start new chat"):
    st.session_state.chat = st.session_state.client.chats.create(model=MODEL_NAME)
    st.session_state.history = []
