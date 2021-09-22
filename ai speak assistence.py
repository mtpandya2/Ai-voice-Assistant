# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:15:47 2021

@author: Nirzari Pandya
"""

import pyttsx3

pip install pyttsx3

import datetime

import speech_recognition as sr



import wikipedia

pip install wikipedia

import smtplib


import webbrowser as wb  

import os

pip install pyaudio  

import pyautogui

pip install pyautogui

import psutil

pip install psutil

import pyjokes

pip install pyjokes



engine=pyttsx3.init()

voice=engine.getProperty('voices')

engine.setProperty('voice',voice[1].id)

newvoicerate=150

engine.setProperty('rate',newvoicerate)
engine.say("This is friday")

engine.runAndWait()


def speak(audio):
    
    engine.say(audio)

    engine.runAndWait()
    
speak("This is friday ai assistant")



def time():
    
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    
    speak(Time)
time()


def date():
    
    year= int(datetime.datetime.now().year)
    
    
    month= int(datetime.datetime.now().month)
    
    date= int(datetime.datetime.now().day)
    
    speak("the current date is")
    
    speak(year)
    speak(month)
    speak(date)

date()


def wishme():
    
    speak("welcome back sir")
    
    time()
    date()
    
    hour= datetime.datetime.now().hour
    
    if hour >=6 and hour <= 12:
        
        speak("good morning")
    
    elif hour >=12 and hour <= 18:
        
        speak("good afternoon")
        
    elif hour >=18 and hour <= 24:
        
        speak("good evening")
        
    else:
        speak("good night")
        
        
    
    
    
    speak("friday at your service. How can i help you?")

wishme()

pip install SpeechRecognition

pip install pyaudio

   


def takecommand():
    
    r= sr.Recognizer()
    
    
    
    
    
    with sr.Microphone() as source:
        
        print("listening....")
        
        r.pause_threshold = 1
        
        audio= r.listen(source)
    
    try:
        
        print("recognizing")
        
        query = r.recognize_google(audio,language='en-in')
        
        print(query)
        
    except Exception as e:
        print(e)
        speak("say that again please")
        
        return "None"

    return query


takecommand()


def sendmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("test@gmail.com","123test")
    server.sendmail("text@gmail.com",to,content)
    server.close()
    
def screenshot():
    
    img=pyautogui.screenshot()
    
    img.save("c:/Users/ss.png")
    
def cpu():
    
    usage=str(psutil.cpu_percent)
    speak("cpu is at "+usage)
    
    battery=psutil.sensors_battery
    speak("battery is at")
    speak(battery.percent)
    
def jokes():
    
    speak(pyjokes.get_joke())

    

if __name__ == "__main__":
    
    wishme()
    
    while True:
        
        query= takecommand().lower()
        
        print(query)
        
        if "time" in query:
            time()
            
        elif "date" in query:
            date()
            
        elif "offlined"  in query:
            quit()
            
        elif "wikipedia" in query:
            speak("searching")
            
            query=query.replace("wikipedia","")
            
            result=wikipedia.summary(query,sentene=2)
            
            speak(result)
            
        elif "send mail" in query:
            
            try:
                speak("what should i say?")
                content=takecommand()
                to="xyz@gmail.com"
                sendmail(to, content)
                speak("email sent succesfully")
                
            except Exception as e:
                
                speak(e)
                
                speak("unable to send")
                
                
        elif "search in chrome in query":
            
            speak("what should i sercah")
            
            chromepath="C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            search= takecommand().lower()
            wb.ge(chromepath).open_new_tab(search+ ".com")
            
        elif "logout" in query :
            
            os.system("shutdown - 1")
            
        elif "logout" in query :
            
            os.system("shutdown /s /t 1")
            
            
        elif "logout" in query :
            
            os.system("shutdown /r /t 1")
            
            
        elif "play songs " in query :
            
            songs_dir ="F:\Music\Music"
            
            songs=os.listdir(songs_dir)
            
            os.startfile(os.path.join(songs_dir,songs[0]))
            
            
            
        elif "remember that" in query :
            
                speak("what should i remember")
                
                data=takecommand()
                
                speak("you said me to remember " + data)
                
                remember = open("data.txt",w)
                
                remember.write(data)
                
                remember.close()
                
                
        elif "do you know anything in query" :
            
            remember = open("data.txt",r)
            
            speak("you said me to remember that" + remember.read())
            
            
            
        elif "screenshot" in query :
            
            screenshot()
            
            speak("Done!")
            
            
        elif "cpu" in query:
            
            cpu()
            
        elif "jokes" in query:
            
            jokes()
            
            
            
            
        
            
            
            
        
            
            
            
            
            
            
                
        
        
            


    