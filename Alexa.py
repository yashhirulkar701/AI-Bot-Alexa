# AI Bot Alexa 

# Imported Libraries
import pyttsx3                   # for voice of Alexa
import datetime as dt            # to collect date and time 
import speech_recognition as sr  # for speech recognition
import wikipedia                 # to search wikipedia
import webbrowser                # to search webbrowser
import os                        # to run os based commands                 
import smtplib                   # to send mail 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
#print(voices[1].id)
engine.setProperty("voice",voices[1].id)

# to make Alexa speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# to make alexa wish
def wishme():
    hour = dt.datetime.now().hour
    if (hour>=0) and (hour<12):
        speak("good morning sir")
        
    elif (hour>=12) and (hour<18):
        speak("good afternoon sir")
        
    else:
        speak("good evening sir")
    speak("I am alexa . Please tell me how may i help you sir")

# to recognize the speech of the user with microphone
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
    
    # if Alexa is not able to recognize              
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

# to send email
def send_email(to,content):

    # using smtp protocol
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # put the email and password to log in the account
    server.login("xyz@gmail.com","<password>")
    server.sendmail("xyz@gmail.com",to,content)
    server.close()

# main function      
if __name__== "__main__":
    
    wishme()
   
    while True:
        query = take_commands().lower()
        
        # to search any query in wikipedia
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("alexa search wikipedia","")
            results =  wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        # to open youtube    
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        
        # to open google    
        elif "open google" in query:
            webbrowser.open("google.com")

        # to open git hub    
        elif "open Git Hub" in query:
            webbrowser.open("www.github.com")
        
         # to play music 
        elif "play music" in query:
            music_dir = 'C:\\Users\\HP\Music\\Love Songs'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        # to show the time    
        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {time}")
        
         # to open pycharm    
        elif "open pycharm" in query:
            path  = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"
            os.startfile(path)   
        
         # receiptent email details    
        elif "email to <ABC>" in query:
            try:
                speak("what shud i say?")
                content = take_commands()
                to = "ABC@gmail.com"
                send_email(to, content)
                speak("email has been sent..!")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to send this message.!")
        
        # to exit Alexa
        elif "buy alexa" in query:
                speak("nice talking to u sir. see you soon.")
                break
            
        
        