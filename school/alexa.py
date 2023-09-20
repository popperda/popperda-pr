import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1.4)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = "no"
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jack' in command:
                talk("online")
                command = command.replace('jack', '')
                print(command)
                return command
            else:
                return command
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if command == "aimo":
        talk('try again bruh')
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is' in command:
        person = command.replace('what is', '')
        try:
            info = wikipedia.summary(person,2)
        except:
            info = "cannot find info on this object"
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, Im taken ')
    elif 'penis' in command:
        talk('give it to me daddy ')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'inspire' in command:
        response = requests.get("https://zenquotes.io/api/random").json()
        quote = response[0]['q']
        print(quote)
        talk(quote)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'thank you' in command:
        talk("no problem")
    else:
        talk('')

while True:
    run_alexa()