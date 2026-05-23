import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from google import genai
import os
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# ============================================================
#   PUT YOUR API KEYS HERE
# ============================================================
GEMINI_API_KEY = "put-your-gemini-key-here"     # from aistudio.google.com
NEWS_API_KEY   = "put-your-newsapi-key-here"    # from newsapi.org
# ============================================================

client = genai.Client(api_key=GEMINI_API_KEY)

recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiProcess(command):
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",  # fix: higher free tier quota
        contents=f"You are a virtual assistant named Jarvis. Give short responses only. User says: {command}"
    )
    return response.text


def processCommand(c):
    print(f"Processing: {c}")

    # Check music library directly — no need to say "play" first
    for song in musicLibrary.music:
        if song in c.lower():
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
            return

    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link = musicLibrary.music.get(song)
        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in the music library.")
    elif "news" in c.lower():
        speak("Here are the top headlines")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news right now.")
    else:
        try:
            output = aiProcess(c)
            speak(output)
        except Exception as e:
            print(f"AI Error: {e}")
            if "429" in str(e):
                speak("AI quota exceeded. Please wait a moment.")
                time.sleep(30)  # wait 30 seconds before retrying
            else:
                speak("Sorry, I couldn't process that request.")


if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

            word = recognizer.recognize_google(audio, language="en-IN")
            print(f"Heard: {word}")
            processCommand(word)

        except sr.WaitTimeoutError:
            print("Timeout, listening again...")
        except sr.UnknownValueError:
            print("Could not understand, listening again...")
        except Exception as e:
            print(f"Error: {e}")