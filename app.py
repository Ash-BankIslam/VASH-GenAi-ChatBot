import streamlit as st
from google import genai   # <-- use google-genai, not google.generativeai

st.title("💬 Gemini Chatbot")

# Initialize client once
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=st.secrets["api_keys"]["gemini"])

# Use the "latest" alias for Flash
MODEL_NAME = "models/gemini-flash-latest"

# Initialize chat once
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model=MODEL_NAME)

# User input (chat-style)
user_input = st.chat_input("Type your message...")

if user_input:
    # Send message to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Show user + Gemini messages in chat bubbles
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response.text)

# Show full conversation history
with st.expander("Conversation history"):
    for turn in st.session_state.chat.history:
        role = "You" if turn.role == "user" else "Gemini"
        for part in turn.parts:
            if hasattr(part, "text"):
                st.write(f"**{role}:** {part.text}")
