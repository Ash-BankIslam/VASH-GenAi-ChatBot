import streamlit as st
from google import genai

st.title("💬 Gemini Chatbot")

# Initialize client once
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=st.secrets["api_keys"]["gemini"])

# Choose a valid model from your list
MODEL_NAME = "models/gemini-flash-latest"

# Initialize chat once
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model=MODEL_NAME)

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Send message to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Display Gemini’s reply
    st.markdown(f"**Gemini:** {response.text}")

    # Show conversation history
    with st.expander("Conversation history"):
        for msg in st.session_state.chat.history:
            role = "You" if msg.role == "user" else "Gemini"
            for part in msg.parts:
                if hasattr(part, "text"):
                    st.write(f"**{role}:** {part.text}")
