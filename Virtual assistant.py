import pyttsx3
import datetime
import webbrowser
import requests
import speech_recognition as sr
import geocoder

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def checking_time():
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour>= 0 and hour<12:
        return 1
    elif hour>= 12 and hour<18:
        return 2
    else:
        return 3

def wishMe():
    t=checking_time()
    if t==1:
        speak("Good Morning ")
  
    elif t==2:
        speak("Good Afternoon ")   
  
    else:
        speak("Good Evening ")  
  
    assname=("I am J D")
    speak(assname)
    speak("How may i help you")

def command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
            

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
  
        except Exception as e:
            print(e)    
            print("Unable to Recognize your voice.")
            speak("Can u repeat it once")
            command()
            return "None"

        return query

def searching(a):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(a)

    
def works_on_query():
    while True:
        query=command().lower()
        if "open youtube" in query:
            searching("https://www.youtube.com/")
            speak("Opening Youtube")
        elif "open google" in query:
            searching(" ")
            speak("Opening Google")
        
        elif "the time" in query:
            strTimeHour = datetime.datetime.now().strftime("%I")
            strTimeMin = datetime.datetime.now().strftime("%M") 
            strTimeAMPM =datetime.datetime.now().strftime("%p") 
            speak(f"Sir, the time is {strTimeHour} {strTimeMin} {strTimeAMPM}")

        elif "weather" in query:
            g = geocoder.ip('me')
            lat=str(g.latlng[0])
            lon=str(g.latlng[1])
            str1="http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=6182220b02c171a870c5450d62234d7f"
            response = requests.get(str1) 
            x = response.json() 
            y = x["main"] 
            current_temperature = y["temp"] 
            current_temperature=round((current_temperature- 273.15),2)
            speak(f"Sir the temperature is {current_temperature} degree Celsius")

        elif "google search" in query:
            url="https://www.google.com/search?q="
            search=query.replace("google search","")
            searching(url+search)
            speak("Getting results for"+search)
        elif "youtube search" in query:
            url="https://www.youtube.com/results?search_query="
            search=query.replace("youtube search","")
            searching(url+search)
            speak("Getting results for"+search)

        elif "no" in query:
            speak("have a great day ahead!!")
            break
        else:
            speak("Sorry Sir. Can u repeat")



        speak("Is there anything else i can do for u?")
        
        

        
        
        
    


if __name__ == '__main__':
    wishMe()
    works_on_query()