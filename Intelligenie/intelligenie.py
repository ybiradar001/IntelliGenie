import pyttsx3
import speech_recognition
import requests
import datetime
from bs4 import BeautifulSoup
import os
import webbrowser
import wikipedia
import pywhatkit
import pyautogui
import random
from plyer import notification
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass



for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

engine =pyttsx3.init("sapi5")
voices =engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.8
        r.energy_threshold = 250
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
if __name__ == "__main__":
    while True:
        speak("Say the magical words to unlock me")
        query = takeCommand().lower()
        if "khul ja sim sim" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "sleep" in query:
                    speak("Ok  , You can call me anytime")
                    break
                
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("genie","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter") 
                
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                #my playlist
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3,4,5) 
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=Oextk-If8HQ")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=hT_nvWreIhg")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=YykjpeuMNEk")
                    elif b==4:
                        webbrowser.open("https://www.youtube.com/watch?v=V8zXLMIjlcw")
                    elif b==5:
                        webbrowser.open("https://www.youtube.com/watch?v=StNb3Jbwm6o")
                
                #youtube controls
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                    
                    
                #email
                elif "email" in query:
                    listener = sr.Recognizer()
                    engine = pyttsx3.init()


                    def talk(text):
                        engine.say(text)
                        engine.runAndWait()


                    def get_info(): 
                        try:    
                            with sr.Microphone() as source:
                                print("listening")
                                voice = listener.listen(source)
                                info = listener.recognize_google(voice)
                                print(info)
                                return info.lower()
                        except:
                            pass    


                    def send_email(receiver, subject, message):
                        server = smtplib.SMTP('smtp.gmail.com',587)
                        server.starttls()
                        server.login('projectananya16@gmail.com', 'ulto kaxn cgya kdrm')
                        #server.login('ananyasaumya16@gmail.com','newme@1609')
                        email = EmailMessage()
                        email['From'] = 'projectananya16@gmail.com'
                        email['To'] = receiver
                        email['Subject'] = subject
                        email.set_content(message)
                        server.send_message(email)


                    email_list = {
                        'yallaling':'biradaryallaling601@gmail.com',
                        'aanchal': 'taanchal03@gmail.com',
                        'apoorva': 'apoorvasaumya07@gmail.com',
                        'ananya': 'ananyasaumya16@gmail.com'
                    }


                    def get_email_info():
                        talk('Hi I am your assistant for today, To Whom you want to send email')
                        name = get_info()
                        receiver = email_list[name]
                        print(receiver)
                        talk('What is the subject of your email?')
                        subject = get_info()
                        talk('Tell me the text in your email')
                        message = get_info()
                        send_email(receiver, subject, message)
                        talk('Thankyou for using me. Your email has been send')
                        talk('Do you want to send more email?')
                        send_more = get_info()
                        if 'yes' in send_more:
                            get_email_info()


                    get_email_info()
                
                elif "microsoft" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "amazon" in query:
                    from SearchNow import searchAmazon
                    searchAmazon(query)   
                elif "myntra" in query:
                    from SearchNow import searchMyntra
                    searchMyntra(query)
                    
                
                 
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                     
                     
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)                     
                                                                        
                
                #elif "what is" in query:
                    #import wikipedia as googleScrap
                    #query = query.replace("Genie","")
                    #query = query.replace("what is","")
                    #query = query.replace("what","")
                    #speak("This is what I found on google")

                    #try:
                        #pywhatkit.search(query)
                        #result = googleScrap.summary(query,1)
                        #speak(result)

                    #except: 
                        #peak("No speakable output available")

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                    
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                
                elif "temperature" in query:
                    search = "temperature in Bengaluru"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif "weather" in query:
                    search = "temperature in Bengaluru"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                 
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                   
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"The time is {strTime}") 
                    
                elif "exit" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "is there any reminder for me" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me" + remember.read())
                
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    query = query.replace("shutdown the system","")
                    query = query.replace("shutdown","")
                    query = query.replace("system","")
                    if "blue" in query:
                        os.system("shutdown /s /t 1")
                    elif "no" in query:
                        break
                   # shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    #if shutdown == "yes":
                     #   os.system("shutdown /s /t 1")

                    #elif shutdown == "no":
                     #   break