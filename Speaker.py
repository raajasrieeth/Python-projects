import pyttsx3 # to be pip installed
# uses the default voices available in your os . The speed and voice settings can be changed from the control panel in Windows.

engine = pyttsx3.init('sapi5')#initialize the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''used for speaking a string given as a parameter.'''
    engine.say(audio)
    engine.runAndWait()
