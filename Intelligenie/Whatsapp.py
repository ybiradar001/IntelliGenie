import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to message?")
    recipient = takeCommand().lower()

    if "aanchal" in recipient:
        speak("What's the message?")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+91**********", message, time_hour=strTime, time_min=update)
        speak("Message sent to Aanchal.")
        
        # Wait for a few seconds to ensure the browser has opened and the message is typed
        sleep(15)
        pyautogui.press('enter')
    elif "yallaling" in recipient:
        speak("What's the message?")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+91**********", message, time_hour=strTime, time_min=update)
        speak("Message sent to ananya.")
        
        # Wait for a few seconds to ensure the browser has opened and the message is typed
        sleep(15)
        pyautogui.press('enter')
    elif "vinayak" in recipient:
        speak("What's the message?")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+91***********", message, time_hour=strTime, time_min=update)
        speak("Message sent to vinayak.")
        
        # Wait for a few seconds to ensure the browser has opened and the message is typed
        sleep(15)
        pyautogui.press('enter')
    elif "pavitra mam" in recipient:
        speak("What's the message?")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+91***********", message, time_hour=strTime, time_min=update)
        speak("Message sent to Pavithra ma'am.")
        
        # Wait for a few seconds to ensure the browser has opened and the message is typed
        sleep(15)
        pyautogui.press('enter')
    else:
        speak("I don't have the number for that contact.")
    
        

if __name__ == "__main__":
    sendMessage()


    
