import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests
import os
from dotenv import load_dotenv
from gemini import ask_gemini
from datetime import datetime
weather_api = os.getenv("WEATHER_API_KEY")

#pip install pocketsphinx
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = MusicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        speak("Fetching latest news")
        r = requests.get(
            f"https://newsapi.org/v2/everything?q=India&sortBy=publishedAt&language=en&apiKey={newsapi}"
        )
        data = r.json()
        articles = data.get("articles", [])
        if not articles:
            speak("Sorry, I couldn't find any news.")
        else:
            for article in articles[:5]:
                print(article["title"])
                speak(article["title"])
    elif "time" in c.lower():
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif "date" in c.lower():
        today = datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")
    elif "day" in c.lower():
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        today = now.strftime("%A, %d %B %Y")
        speak(f"Today is {today}. The time is {current_time}.")
    elif "weather" in c.lower():
        city = c.lower().replace("weather in", "").strip()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            speak(
                f"The current temperature in {city} is {temperature} degrees Celsius."
            )

            speak(f"The weather is {description}.")

            speak(f"The humidity is {humidity} percent.")

        else:
            speak("Sorry, I couldn't fetch the weather.")
    else:
        speak("Thinking...")
        reply = ask_gemini(c)
        if len(reply) > 500:
            reply = reply[:500]
        print(reply)
        speak(reply)
    



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone

        r = recognizer
        
        # recognize speech using Sphinx
        print("Recognizing....")
        try:
            # with sr.Microphone() as source:
            #     print("listening...")
            #     audio = r.listen(source,timeout=3,phrase_time_limit=4)
            with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    print("Listening...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=4)
            word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))




