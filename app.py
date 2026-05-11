import streamlit as st
import google.generativeai as genai

st.title("💬 Gemini Chatbot")

# Configure Gemini with your secret key
genai.configure(api_key=st.secrets["api_keys"]["gemini"])

# Use the "latest" alias for Flash
MODEL_NAME = "models/gemini-flash-latest"

# Initialize chat session once
if "chat" not in st.session_state:
    model = genai.GenerativeModel(MODEL_NAME)
    st.session_state.chat = model.start_chat(history=[])

# Chat-style input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Send message to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Show user + Gemini messages in chat bubbles
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response.text)

# Show full conversation history (like Gemini web)
with st.expander("Conversation history"):
    for msg in st.session_state.chat.history:
        role = "You" if msg.role == "user" else "Gemini"
        if msg.parts and hasattr(msg.parts[0], "text"):
            st.write(f"**{role}:** {msg.parts[0].text}")
