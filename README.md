Llama 2 Chatbot with Streamlit and Voice Output

Welcome to the Llama 2 Chatbot project! This is a web-based chatbot built using Streamlit, powered by the Llama 2 model via the Ollama framework, and enhanced with voice output functionality using Google Text-to-Speech (gTTS). The chatbot provides a clean, interactive interface for chatting with the Llama 2 model, with optional voice output that can be enabled or disabled.

Features

Interactive Chat Interface: A user-friendly web interface built with Streamlit, allowing users to chat with the Llama 2 model.

Chat History: Maintains a persistent chat history displayed in the interface, with distinct styling for user and bot messages.

Voice Output: Users can enable or disable voice output via a toggle button. When enabled, the bot’s responses are converted to speech and played directly (autoplays without displaying audio controls). The voice output is shortened for brevity (default 100 characters max, adjustable).

Clear Chat: A button to reset the chat history and remove any associated audio files.

Local Model Support: Uses the Llama 2 model running locally via Ollama, ensuring privacy and offline capability (with the model downloaded).

How We Built It

This project was developed with the following technologies and steps:

Streamlit: We used Streamlit to create a responsive, web-based interface for the chatbot. The interface includes custom CSS for a clean look, chat history display, input area, and buttons for sending messages and clearing the chat.

Ollama: The Llama 2 model is hosted locally using Ollama, a framework for running large language models (LLMs) on your machine. We integrated the Ollama Python client to communicate with the llama2:latest model, fetching responses for user inputs.

gTTS (Google Text-to-Speech): For voice output, we implemented gTTS to convert the bot’s text responses into MP3 audio files, which are then played directly in the Streamlit app using HTML5 audio tags and base64 encoding.

Python Libraries:

streamlit for the web interface.

ollama for interacting with the Llama 2 model.

gTTS for text-to-speech conversion.

Standard libraries like os, datetime, base64, logging, and time for file handling, timing, and debugging.

Development Process:

Started with a basic Streamlit chat interface.

Integrated Ollama to connect to the locally running Llama 2 model.

Added voice output functionality with a toggle button, initially displaying audio players, then updated to autoplay directly without visible controls.

Implemented chat history persistence using Streamlit’s session state.

Added features like text truncation for voice output and error handling for robust operation.

Prerequisites

Before running this project, ensure you have the following installed on your PC:

Python 3.8+: Check your Python version with python --version or python3 --version.

pip: Python’s package installer, typically included with Python.

Ollama: Required to run the Llama 2 model locally.

Internet Connection: Needed initially to pull the Llama 2 model and for gTTS to generate voice output.

Installation and Setup

Follow these steps to set up and run the project on your PC:

1. Clone the Repository

Clone this repository to your local machine:

git clone <repository-url>
cd llama2-chatbot-streamlit

Replace <repository-url> with the actual GitHub URL of your repository.

2. Install Python Dependencies

Install the required Python packages using the provided requirements.txt:

pip install -r requirements.txt

If requirements.txt isn’t present, create it with the following content:

streamlit>=1.30.0
ollama>=0.1.0
gTTS>=2.5.0

Then run:

pip install -r requirements.txt

3. Set Up Ollama and Run the Llama 2 Model Locally

Ollama is used to host and run the Llama 2 model locally. Follow these steps:

Install Ollama

Download and install Ollama for your operating system from the official website: Ollama Downloads.

For Linux/MacOS:

curl -fsSL https://ollama.com/install.sh | sh

For Windows, download the installer from the Ollama website and follow the installation instructions.

Pull the Llama 2 Model

Open a terminal and run the following command to pull the llama2:latest model:

ollama pull llama2:latest

This downloads the Llama 2 model to your local machine. It may take some time depending on your internet speed and system resources.

Run the Ollama Server

Start the Ollama server in the background to host the model:

ollama serve

This command runs the Ollama server, which the Python script will connect to for generating responses. You can leave this running in a separate terminal window or run it in the background.

4. Run the Streamlit App

With Ollama running and dependencies installed, launch the Streamlit app:

streamlit run app.py

This will open the chatbot interface in your default web browser at http://localhost:8501.

5. Using the Chatbot

Type a message in the input area and click "Send" to receive a response from the Llama 2 model.

Use the "Enable Voice Output" toggle to enable or disable voice output. When enabled, the bot’s responses will play directly as audio without displaying any audio controls.

Click "Clear Chat" to reset the chat history and remove any temporary files.

Troubleshooting

Audio Not Playing: Ensure your browser allows autoplay for localhost:8501. Some browsers block autoplay; you may need to interact with the page (e.g., click a button) or adjust browser settings.

Ollama Connection Issues: Verify the Ollama server is running (ollama serve) and the Llama 2 model is pulled (ollama pull llama2:latest).

gTTS Errors: Ensure you have an internet connection, as gTTS relies on Google’s API. Verify gTTS is installed (pip install gTTS).

Dependencies: If you encounter errors, ensure all packages in requirements.txt are installed and compatible with your Python version.

Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome, especially for enhancing voice output, adding new features, or improving UI/UX.

License

This project is licensed under the MIT License - see the LICENSE file for details (if applicable, create a LICENSE file with appropriate terms).

Acknowledgments

Ollama: For providing a framework to run Llama 2 locally.

Streamlit: For the excellent web framework for data apps and chat interfaces.

gTTS: For enabling text-to-speech functionality.

Llama 2: For powering the chatbot with its advanced language capabilities.

If you have any questions or need assistance, feel free to open an issue on GitHub or contact hemasriram111@gmail.com
