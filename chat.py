import requests
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import time
import os

engine = pyttsx3.init()
r = sr.Recognizer()

def Speak(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

tts = gTTS('Hello, I am Robot. A ChatGPT Powered Chatbot.')
tts.save("speech.mp3")
os.system("speech.mp3")
time.sleep(5)
counter = 0
while True:
    with sr.Microphone() as source2:
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=0.2)
            
        #listens for the user's input
        audio2 = r.listen(source2)
            
        # Using google to recognize audio
        MyText = r.recognize_google(audio2)
        output = requests.get("http://172.105.28.74:8000/chatgpt?username=Skyler Fischer&password=30212178Skyler&message=" + MyText).text
        print(output[5:])
        tts = gTTS(output[5:])
        tts.save("speech.mp3")
        os.system("speech.mp3")
