import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
#import os

engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')#getting details of current voice
engine.setProperty("voice", voice[0].id)

rate=engine.getProperty("rate")
engine.setProperty('rate',150)

volume=engine.getProperty('volume')
engine.setProperty("volume",1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()##Without this command, speech will not be audible to us.

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query




if __name__ == '__main__':
        speak("Welcome to Desktop Assistant")
        wishMe()
        while True:
            query=takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                # query=query.replace('wikipedia',"")
                results=wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'how are you' in query:
                speak("I am fine Sir, How are you?")

            elif 'your name' in query:
                speak("Jarvis Sir")

            # elif '' in query:
            #     speak("I am waiting for your command Sir")

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")


            elif 'open google' in query:
                webbrowser.open("google.com")
                #speak("Khool Gaya Google Sir")

            elif 'quit' in query:
                speak("OK Sir, It was my pleasure to help you!")
                break

            elif 'open codechef' in query:
                webbrowser.open("codechef.com")

            elif 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir the time is {strTime}")








