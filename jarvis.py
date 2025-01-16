import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API Key from environment variables
newsapi = os.getenv("NEWSAPI_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Silent Mode variable to control the state of silent mode
silent_mode = False  # Tracks if silent mode is active

# Function to speak text, only if silent mode is off
def speak(text):
    """Speak the provided text if silent mode is off."""
    if not silent_mode:
        engine.say(text)
        engine.runAndWait()

# Function to process user commands
def processCommand(c):
    """Process the user's command."""
    global silent_mode

    print(c)
    c = c.lower().strip()

    if "stop" in c:
        speak("Stopping execution. Goodbye!")  # Speak when stopping
        exit(0)

    elif "silent mode" in c:
        speak("Silent mode activated. Say 'wake up' to disable it.")  # Speak when silent mode is activated
        silent_mode = True

    elif "wake up" in c:
        silent_mode = False
        speak("Silent mode deactivated. How can I help you?")  # Speak when silent mode is deactivated

    elif "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found in your library.")  # Inform if the song is not found in the library
    elif "news" in c:
        fetch_and_speak_news()  # Fetch and speak news headlines


# Function to fetch and read top news headlines
def fetch_and_speak_news():
    """Fetch and read top news headlines."""
    try:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Limit to the top 5 headlines
                speak(article['title'])
        else:
            speak("Unable to fetch news at the moment.")  # Handle error in fetching news
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("An error occurred while fetching the news.")  # Error handling for news fetching

# Main program loop for listening and processing commands
if __name__ == "__main__":
    speak("Initializing Jarvis...")  # Speak when starting

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduce background noise
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                print(f"Recognized: {word}")

                if "jarvis" in word.lower():
                    speak("I'm listening. What can I do for you?")  # Speak when activating Jarvis
                    with sr.Microphone() as command_source:
                        recognizer.adjust_for_ambient_noise(command_source, duration=0.5)
                        print("Waiting for command...")
                        audio = recognizer.listen(command_source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)  # Process the recognized command
        except sr.WaitTimeoutError:
            print("Listening timeout. Please try again.")  # Handle timeout error
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")  # Handle unknown value error
        except Exception as e:
            print(f"Error: {e}")  # Handle any other errors
