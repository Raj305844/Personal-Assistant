import speech_recognition as sr
import webbrowser
import pyttsx3 # For text-to-speech conversion
import musiclibrary
import requests # For making HTTP requests (News API)
import os # For system operations like shutdown and restart

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Your Own News API"

# Function to process voice commands
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():

        # Fetch latest news headlines using NewsAPI

        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=")  # This is link already provided when you for News API
        if r.status_code == 200:
            
            data = r.json() # Parse response

            articles = data.get('articles',[])

            for article in articles[:2]:
                speak(article['title'])

    elif "shutdown" in c.lower():
        os.system("shutdown /s")

    elif "restart" in c.lower():
        os.system("shutdown /r")


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:

        r = sr.Recognizer()  # Initialize recognizer each time for new input

        print("rcongnizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=None, phrase_time_limit=None)
            word = r.recognize_google(audio)

            if(word.lower()=="jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

            print(word)
        except Exception as e:
            print("Error:".format(e))  # Print any errors during speech recognition