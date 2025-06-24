import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # Slower speaking rate
    engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Robotic default
    engine.say(text)
    engine.runAndWait()
# engine = pyttsx3.init()
# engine.setProperty('rate', 160)  # Slower speaking rate
# engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Robotic default
# engine.say("test")
# engine.runAndWait()