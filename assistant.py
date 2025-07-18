import datetime
import os
import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
def talk(text):
    print("🎙️ PUJ:", text)
    engine.say(text)
    engine.runAndWait() 
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")    
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command
def run_puj():
    command = take_command()
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing on YouTube 🎶")
        pywhatkit.playonyt(song)
    elif "what's the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")
    elif "who is uday codes" in command or "who is uday_codes" in command:
        info = (
            "Uday, known as uday_codes on Instagram, is a coding content creator. "
            "He teaches Python projects in Telugu and runs udaycodes.in 💻"
        )
        talk(info)
    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")
    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")
    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()
    elif command != "":
        talk("I heard you, but I don’t understand that yet 😅")
talk("Yo! I'm PUJ – your personal voice assistant 💡")
while True:
    run_puj()
