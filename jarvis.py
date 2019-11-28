import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I am JARVIS, Ready to Help You")

def takecomman():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.energy_threshold = 150
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print("say that again please")
        query = None
        return "None"
    return query

if __name__ == '__main__':
    speak("runing process's.....")
    speak("starting ai system.....")
    speak("runing JARVIS ai system.....")
    speak("started ai system.....")
    speak("JARVIS system is online.....")
    wishme()
    while True:
        query = takecomman().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences= 5)
            speak("According to wikipedia.....")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            my_dir = "C:\\Users\\Public\\Music\\Sample Music"
            songs = os.listdir(my_dir)
            os.startfile(os.path.join(my_dir,songs[2]))
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%h:%m:%s")
            print(int(time))
            speak(f"sir the time is: {time}")
        elif 'open code' in query:
            cp = "C:\\Users\\DARSHAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cp)
        elif 'hi' in query:
            speak("Hi Sir")
        else:
            speak("ok sir")