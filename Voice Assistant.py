import pyttsx3  # This module convert text to speech
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes


def speec_text():
    recognizer = sr.Recognizer()  # Speech recognizer
    with sr.Microphone() as Source:  # Microphone is like ear of recognizer

        print("Listening.......")
        recognizer.adjust_for_ambient_noise(Source)  # this line is for remove noise
        audio = recognizer.listen(Source)

        try:
            print("Recognizing.....")
            data = recognizer.recognize_google(audio)
            print(data)
        except sr.UnknownValueError:
            print("Sorry not understood")

speec_text()
