#speech engine
from tkinter import *
from interface import window
import pyttsx3

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',140)

def speak(que):
    engine.say(que)
    engine.runAndWait()

import datetime

def wishMe(a):
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        sp='good morning!'+ a +'i am anonymous'
        speak(sp)
        print("Good morning!",a)
        wish='Good Morning!'+ ' '+a
        return wish
  
    elif hour>= 12 and hour<18:
        sp='good afternoon!'+ a +'i am anonymous'
        speak(sp)
        print("Good afternoon!",a)
        wish='Good Afternoon!'+ ' '+a
        return wish 
  
    else:
        sp='good evening!'+ a +' '+'i am anonymous'
        speak(sp)
        print("Good evening!",a)
        wish='Good evening!'+ ' '+a
        return wish



#microphone engine

import speech_recognition as sr

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"{query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

#useraccess

accdic={'an01':'Harsha','an02':'praveen'}

