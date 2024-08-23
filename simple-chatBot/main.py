# 1. Importing necessary libraries
import streamlit as st
import random 
import time 

# 2. Creating a title for our streamlit web application
st.title("Simple chat")

# 3. Initializing the chat history in the session state (How the chatbot tracks things)
if "messages" not in st.session_state: # Check if the "message" exists in session
    st.session_state.message = [] # Initialize "message" as an empty list

# 4. Displaying the existing chat messages from the user and the chatbot
for message in st.session_state.message: # For every message in the chat history
    with st.chat_message(message["role"]): # Create a chat messge box
        st.markdown(message["content"]) # Display the content of the message


# 5. Accepting the user intput and adding it to the message history
if prompt := st.chat_input("What is up?"): # If user enters a message
    with st.chat_message("user"): # Display user's message in a chat message box
        st.markdown(prompt) # Display the user's message
    st.session_state.message.append({"role": "user", "content" : prompt}) # Adding user's message to the chat History

# 6. Generating and displaying the assistant's response
with st.chat_message("assistant"): # Create a chat message box for assistant's response
    message_placeholder = st.empty() # Create an empty placeholder for the assistant's msg
    full_response = "" # Initialize an empty string for the full response
    assistant_response = random.choice([
        "Hi there! How can I assist you today?",
        "Hi! Is there anything I can help you with?",
        "Do you need help?"
    ]) # Select the assistant's response randomly

    # Simulate "typing" effect by gradually revealing the response
    for chunk in assistant_response.split(): # For each word in the response
        full_response += chunk + " "
        time.sleep(0.005) # Small delay between each word, for smooth animation
        message_placeholder.markdown(full_response + " ") # Update place_holder with curr response & a blinking cursor

    message_placeholder.markdown(full_response) # Remove cursor & display full resp
    st.session_state.message.append({"role": "assistant", "content" : full_response})