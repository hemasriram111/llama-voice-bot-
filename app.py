import streamlit as st
import ollama
from gtts import gTTS
import os
from datetime import datetime
import base64
import logging
import time

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(page_title="Llama 2 Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for clean UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .stTextInput, .stButton {
        border-radius: 5px;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .bot-message {
        background-color: #e8f5e9;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize chat history and voice setting in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'voice_enabled' not in st.session_state:
    st.session_state.voice_enabled = False

# Function to play audio directly in Streamlit (autoplays)
def play_audio(audio_file):
    try:
        with open(audio_file, "rb") as f:
            audio_data = f.read()
            b64 = base64.b64encode(audio_data).decode()
            md = f"""
            <audio autoplay="true" style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            Your browser does not support the audio element.
            </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
        # Delay before removing the file to ensure playback (e.g., 5 seconds)
        time.sleep(5)  # Adjust this delay as needed (e.g., 5 seconds for playback)
        os.remove(audio_file)  # Clean up the temporary file
        logger.info(f"Played and removed audio file: {audio_file}")
    except Exception as e:
        logger.error(f"Error playing audio: {str(e)}")
        st.error(f"Failed to play audio: {str(e)}")

# Function to shorten text for voice output
def shorten_text(text, max_length=100):
    if len(text) > max_length:
        # Truncate to max_length and add ellipsis
        return text[:max_length].rsplit(' ', 1)[0] + "..."
    return text

# Title
st.title("Llama 2 Chatbot 🤖")

# Voice toggle button
st.session_state.voice_enabled = st.toggle("Enable Voice Output", value=st.session_state.voice_enabled)

# Display chat history
st.subheader("Chat History")
for message in st.session_state.chat_history:
    if message['role'] == 'user':
        st.markdown(f'<div class="user-message">You: {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">Chatbot: {message["content"]}</div>', unsafe_allow_html=True)

# Input area
user_input = st.text_input("Your message:", key="user_input")

# Send button
if st.button("Send"):
    if user_input.strip():
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get response from Llama 2
        try:
            response = ollama.chat(model="llama2:latest", messages=[
                {"role": "user", "content": user_input}
            ])
            bot_response = response['message']['content']
            
            # Add full bot response to history
            st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
            
            # Display full text response
            st.markdown(f'<div class="bot-message">Chatbot: {bot_response}</div>', unsafe_allow_html=True)
            
            # If voice is enabled, generate and play audio directly (no visible player)
            if st.session_state.voice_enabled:
                # Shorten the text for voice output
                short_response = shorten_text(bot_response)
                logger.info(f"Generating voice for: {short_response}")
                audio_file = "response.mp3"
                tts = gTTS(text=short_response, lang='en', slow=False)
                tts.save(audio_file)
                play_audio(audio_file)
            
            # Rerun to update the UI with the new messages
            st.rerun()
            
        except Exception as e:
            logger.error(f"Error in chatbot response: {str(e)}")
            st.error(f"Error: {str(e)}")

# Clear history button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Footer
st.markdown("---")
st.markdown("Powered by Llama 2, Streamlit, and gTTS")

# Auto-scroll to bottom
st.markdown("""
    <script>
    window.scrollTo(0, document.body.scrollHeight);
    </script>
""", unsafe_allow_html=True)