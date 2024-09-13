import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # Corrected method name
    engine.setProperty('rate', rate - 70)  # Corrected method name and value
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text")