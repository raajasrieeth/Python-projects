import pyttsx3 # to be pip installed
import work_withPDf

engine = pyttsx3.init('sapi5')#initialize the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak(text)