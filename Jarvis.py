import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis ma'am. Please tell me how may I help you?")


def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        # r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<Email_Address>', '<Email_Password>')           # Email From
    server.sendmail('<Email_Address>', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia..")
            print(results)
            speak(results) 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'play music' in query:
            music_dir = "E:\\Kirtan 2020"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\gyanc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'send email' in query:
            try:
                speak("What should I say ma'am?")
                content = takeCommand()
                to = "<Your_Email>"            # Email - To
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ma'am! I am not able to send this email") 

        elif 'quit' in query:
            speak("Quitting ma'am. Thanks for your time.")
            exit()


