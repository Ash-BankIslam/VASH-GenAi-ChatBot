import streamlit as st
from google import genai

# Configure Gemini client with secret key
client = genai.Client(api_key=st.secrets["api_keys"]["gemini"])

# Choose a valid model from your list
MODEL_NAME = "models/gemini-2.5-flash"   # or "models/gemini-flash-latest"

st.title("💬 Gemini Chatbot")

# Initialize chat session in Streamlit state
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(model=MODEL_NAME)

# User input box
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
            # Each message may have multiple parts; display text parts
            for part in msg.parts:
                if hasattr(part, "text"):
                    st.write(f"**{role}:** {part.text}")
