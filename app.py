import streamlit as st
import google.generativeai as genai

st.title("💬 Gemini Chatbot")

# Configure Gemini with your secret key
genai.configure(api_key=st.secrets["api_keys"]["gemini"])

MODEL_NAME = "gemini-1.5-flash"  # or "gemini-1.5-pro" for deeper reasoning

# Initialize chat once
if "chat" not in st.session_state:
    model = genai.GenerativeModel(MODEL_NAME)
    st.session_state.chat = model.start_chat(history=[])

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
