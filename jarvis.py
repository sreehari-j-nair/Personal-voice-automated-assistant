import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import datetime
import time
import instabot
import mailautomate
import wikipedia
import requests
from bs4 import BeautifulSoup

#initaiting recognizer and pyttsx3
r=sr.Recognizer()
engine=pyttsx3.init()

global speak

#function for main speaker
def speak(voc):
    engine.say(voc)
    engine.runAndWait()

#function for search
def search():
    print("initiating the search protocol")
    engine.say("What do you want to search for")
    engine.runAndWait()
    while True:
        try:
            with sr.Microphone() as source:
                cmdaudio = r.listen(source)
                cmdtext=r.recognize_google(cmdaudio)
                cmdvoc=format(cmdtext)
                if "leave it" in cmdvoc:
                    engine.say("Fine sir")
                    engine.runAndWait()
                    break
                else:
                    webbrowser.open_new('https://google.com/search?q=' + cmdvoc)
                    engine.say("This is what I found for"+ cmdvoc)
                    engine.runAndWait()
                    break
        except:
            engine.say("Sorry sir not clear")
            engine.runAndWait()
            continue

#function for tracing location
def location():
    print("initiating the location trace protocol")
    engine.say("Which location want to trace sir")
    engine.runAndWait()
    while True:
        try:
            with sr.Microphone() as source:
                cmdaudio = r.listen(source)
                cmdtext=r.recognize_google(cmdaudio)
                cmdvoc=format(cmdtext)
                if "leave it" in cmdvoc:
                    engine.say("Fine sir")
                    engine.runAndWait()
                    break
                else:
                    webbrowser.open_new('https://google.nl/maps/place/' + cmdvoc +'/&amp;')
                    engine.say("This is the location for"+ cmdvoc)
                    engine.runAndWait()
                    break
        except:
            engine.say("Sorry sir not clear")
            engine.runAndWait()
            continue

#function for sendind mail
def mail():
    print("Initiating mail protocol")
    mailautomate.mailsend()

#function for finding the time
def timer():
    print("Initiating time protocol")
    time=datetime.datetime.today()
    t=time.hour
    t1=time.minute
    if t >=1 and t <12:
        engine.say(f"Sir its about{t}{t1} AM ")
        engine.runAndWait()
    else:
        engine.say(f"sir its about{t}{t1} PM")
        engine.runAndWait()

#function for opening applications
def open(voc):
    voice=voc.partition("open")
    app=str(voice[2])
    app=app.lower()
    os.system(app)

#general introduction about the day
def general():
    engine.say("Fresh and online sir")
    engine.runAndWait()

#function for checking the instagram
def insta():
    print("initiating the instagram protocol")
    instabot.instagram()

#function for room automation

#function for searching in wikipedia
def wiki(voc):
    voice=voc.partition("Wikipedia")
    subject=str(voice[2])
    result=wikipedia.summary(subject,sentences=3)
    resultspeech="Sir, According to wikipedia"+ result
    engine.say(resultspeech)
    engine.runAndWait()

        
#function for main voice receiving
def command():
    time = datetime.datetime.today()
    time1=time.hour
    if time1 >= 1 and time1 < 12 :
        speak("Good morning sir , Welcome back to the system")
    elif time1 >=12 and time1 < 17:
        speak("Good afternoon sir, Welcome back to the system")
    elif time1 >= 17 and time1 < 20:
        speak("Good evening sir, welcome back to the system")
    else:
        speak("Already late sir, You may shutdown the system and may sleep")
    while True:
        try:
            with sr.Microphone() as source:
                cmdaudio = r.listen(source)
                cmdtext=r.recognize_google(cmdaudio)
                cmdvoc=format(cmdtext)
                cmdvoc.lower()
                print(cmdvoc)
                if "hello" in cmdvoc:
                    speak("Hi sir")
                elif "today" and "how" in cmdvoc:
                    general()
                elif "open" in cmdvoc:
                    open(cmdvoc)
                elif "search" in cmdvoc:
                    search()
                elif "location" in cmdvoc:
                    location()
                elif "time" in cmdvoc:
                    timer()
                elif "send" and "message" in cmdvoc:
                    mail()
                elif "open" and "Instagram" in cmdvoc:
                    insta()
                elif "Wikipedia" in cmdvoc:
                    wiki(cmdvoc)
                elif "sleep" in cmdvoc:
                    speak("As you wish sir, I will be at your command")
                    break
                else:
                    speak("command not in list sir")
        except:
            continue

#main intiatition of the code
password=input("Enter the passcode: ")
if password=="jarviscx3":
    engine.say("Initiating the progam sir, presently at the sleep mode")
    engine.runAndWait()
    while True:
        try:
            with sr.Microphone() as source:
                cmdaudio = r.listen(source)
                cmdtext=r.recognize_google(cmdaudio)
                cmdvoc=format(cmdtext)
                cmdvoc.lower()
                print(cmdvoc)
                if "wake up" in cmdvoc:
                    command()
                elif "shutdown" and "program" in cmdvoc:
                    speak("Fine sir, terminating the protocols")
                    break
                else:
                    continue
        except:
            print("continue")
            continue
else:
    print("Incorrect password")