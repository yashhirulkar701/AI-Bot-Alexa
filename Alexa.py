# AI Bot Alexa 

import pyttsx3
import datetime as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import datetime
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
#print(voices[1].id)
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = dt.datetime.now().hour
    if (hour>=0) and (hour<12):
        speak("good morning sir")
        
    elif (hour>=12) and (hour<18):
        speak("good afternoon sir")
        
    else:
        speak("good evening sir")
    speak("I am alexa . Please tell me how may i help you sir")

def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:",query)
              
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def send_email(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("yashhirulkar701@gmail.com","jyotihirulkar")
    server.sendmail("yashhirulkar701@gmail.com",to,content)
    server.close()

      
if __name__== "__main__":
    
    wishme()
   
    while True:
        query = take_commands().lower()
        
        #logic for executing tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("alexa search wikipedia","")
            results =  wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com")
            
        elif "open docker hub" in query:
            webbrowser.open("hub.docker.com")
        
        elif "play music" in query:
            music_dir = 'C:\\Users\\HP\Music\\Love Songs'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {time}")
            
        elif "open pycharm" in query:
            path  = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(path)   
            
        elif "email to yash" in query:
            try:
                speak("what shud i say?")
                content = take_commands()
                to = "yashhirulkar701@gmail.com"
                send_email(to, content)
                speak("email has been sent..!")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this message.!")
        
        elif "buy alexa" in query:
                speak("nice talking to u sir. see you soon.")
                break
            
        
        