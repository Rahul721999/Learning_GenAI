import streamlit as st
import google.generativeai as genai

# Configure the Google Gemini API key
genai.configure(api_key="")

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit app title
st.title("Simple Chatbot")

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
user_input = st.chat_input("What is up?")

if user_input:
    # Display user's message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Add user's message to the history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response using Google Gemini
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        # Generate content with the model
        response = model.generate_content(user_input)
        assistant_response = response.text

        # Simulate typing effect
        for chunk in assistant_response.split():
            full_response += chunk + " "
            response_placeholder.markdown(full_response + " ")

        response_placeholder.markdown(full_response)

        # Add assistant's response to the history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
