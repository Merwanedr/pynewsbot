import pyttsx3
import requests
import speech_recognition as sr
import os
import platform
from time import sleep
from colorama import init, Fore

init()

country = 'country=us'
apiKey = ''

r = requests.get('https://newsapi.org/v2/top-headlines?'+country+'&apiKey='+apiKey)
articles = r.json()['articles']

if platform.system() == 'Darwin':
    os.system('clear')
elif platform.system() == 'Linux':
    os.system('clear')
elif platform.system() == 'Windows':
    os.system('cls')

# Text to speech function
def talkToMe(audio):
    print(Fore.CYAN+audio)
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()

# Initiate command function
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.RED+'I am waiting for your command...')
        audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio)
        print(Fore.RED+'You said: '+Fore.GREEN+ command + '\n')
    
    except sr.UnknownValueError:
        assistant(myCommand())
    
    return command

def news():
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    for article in articles:
        print('\n')
        print(Fore.RED+'-------------------------------------------------')
        engine.say('from')
        engine.say(article['source']['name'])
        engine.say('by')
        engine.say(article['author'])
        print(Fore.GREEN+'From :')
        print(article['source']['name'])
        print(Fore.GREEN+'By :')
        print(article['author'])
        print(Fore.CYAN + article['title'])
        engine.say(article['title'])
        engine.say('Description.')
        print(Fore.RED + 'Description : ')
        print(Fore.WHITE+article['description'])
        print(Fore.RED+'-------------------------------------------------')
        print('\n')
        engine.say(article['description'])
    engine.runAndWait()

# Main function
def assistant(command):
    if 'news' in command:
        talkToMe('Here are some of the headlines.')
        sleep(2)
        news()
    else:
        talkToMe('Sorry, I did not understand your command')


talkToMe('Hi. What do you want to hear?')


while True:
    assistant(myCommand())