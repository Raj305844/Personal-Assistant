# Jarvis - Voice-Controlled Personal Assistant

A Python-based voice assistant that listens to your commands and performs a variety of tasks. Designed to simplify everyday activities like browsing websites, playing music, fetching the latest news, or controlling system operations like shutdown or restart.

---

## Features
- **Open Websites**: Commands like *"Open Google"* or *"Open YouTube"* will launch the respective websites.
- **Play Music**: Play songs using predefined links in a music library.
- **Fetch News**: Get the latest top headlines using the News API.
- **System Control**: Commands to shutdown or restart the system.
- **Activation Keyword**: The assistant is activated when you say the word **"Jarvis"**.

---

## Prerequisites
To run this project, you'll need:
- Python 3.8+ installed.
- Required libraries:
  - `speech_recognition`
  - `pyttsx3`
  - `requests`
  - `webbrowser`

You can install the required libraries using:
```bash
pip install speechrecognition pyttsx3 requests



## Usage
1. Run the program
        python jarvis.py

2. Speak "Jarvis" to activate the assistant.

3. After activation, give your command:
    *   "open google"
    *   "Play [song_name]"
    *   "Tell me the news"
    *   "Shutdown" or "Restart"


----Limitations
+ Internet connection is required for features like opening websites, playing music, and fetching news.
+ The musiclibrary.py file should be manually populated with song links.

