import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone

        r = sr.Recognizer()

        # recognize speech using Sphinx
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=4)
            word = r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))




