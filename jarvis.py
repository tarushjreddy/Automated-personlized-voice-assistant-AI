from datetime import datetime
import pyttsx3
import pyaudio
import wikipedia
import os
import sys
import subprocess
import webbrowser
import smtplib
import speech_recognition as sr
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate

engine.setProperty('rate', 210)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
print(voices[0].id)
# engine.say("hello")

engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Greet():

    time = int(datetime.datetime.now().hour)
    print(time)

    if time > 6:
        speak("Good Morning!!! How can i help you?")
    elif time > 12:
        speak("Good Afternoon!!! How can i help you?")
    elif time > 18:
        speak("Good Evening!!! How can i help you?")
    elif time > 21 or time < 6:
        speak("Good Night!!! How can i help you?")


def sendEmail(to, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("developerkingpro@gmail.com", "Tarushjreddy9*")
    server.sendmail("developerkingpro@gmail.com", to, message)
    server.close()


def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogninzing....")
        # print("processing......")
        query = r.recognize_google(audio, language='en-in')
        # print(f"user said {query}")

    except Exception as e:
        # print(e)
        print("Say that again please")
        speak("Sorry can u speak again please")
        return "None"

    return query


if __name__ == "__main__":
    # speak("macbook pro")
    while True:
        speak("How can I help you...")
        query = take().lower()
        print(query)
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
        # if query == "quit":
        #     speak("thank you good bye!!")
        elif "open youtube" in query:
            speak("opening Youtube..")
            webbrowser.open("http://www.youtube.com")
        elif "open google" in query:
            speak("opening google..")
            webbrowser.open("http://www.google.com")
        elif "open stack overflow" in query:
            speak("opening Google..")
            webbrowser.open("https://stackoverflow.com")
        elif "play music" in query:
            speak("playing music..")
            speak("change default folder to listen more music...")
            music = "WhatsApp Audio 2020-11-03 at 3.22.12 PM (2).mpeg"
            # songs = os.listdir(music)
            # print(songs)
            subprocess.call(["open", music])
        elif "the time" in query:
            from datetime import datetime

            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        # elif "sangeetha" in query:
        #     speak("sangeetha is the richest person in the world")
        elif "open code" in query:
            speak("Please change the root directory if any error")
            #subprocess.call(["open", "music"])
        elif "send email" in query:
            try:
                speak("please narrate the message..")
                message = take()
                to = "tarushjreddy63@gmail.com"
                sendEmail(to, message)
                speak("email sent")
            except Exception as e:
                speak("error")
                print(e)
        elif "quit" in query:
            speak("thank you verry much!!!")
            exit()
