import streamlit as st
import google.generativeai as genai

# Configure Gemini with secret key
genai.configure(api_key=st.secrets["api_keys"]["gemini"])

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("💬 Gemini Chatbot")

# Session state for conversation history
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Send message to Gemini
    response = st.session_state.chat.send_message(user_input)

    # Display response
    st.markdown(f"**Gemini:** {response.text}")

    # Show conversation history
    with st.expander("Conversation history"):
        for msg in st.session_state.chat.history:
            role = "You" if msg.role == "user" else "Gemini"
            st.write(f"**{role}:** {msg.parts[0].text}")
