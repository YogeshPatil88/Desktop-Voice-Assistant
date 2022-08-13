from email.mime import audio
from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")
    speak("Hello I am Jarvis Sir, How may I help You")

def takecommand():
    #It takes the command from microphone and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please say that again")
        return "None"
    return query

if __name__=='__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        #Logic for executiong tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            results = wikipedia.summary(query,sentences=1)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir="D:\\MUSIC"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'quit' in query:
            exit()