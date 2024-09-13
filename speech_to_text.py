import speech_recognition as sr
def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Say something:")
            audio = r.listen(source)

        voice_data = r.recognize_google(audio)
        print("You said:", voice_data)
        return voice_data

    except sr.UnknownValueError:
        print("Error: Could not understand audio")
        return None

    except sr.RequestError as e:
        print(f"RequestError: {e}")
        return None

    except OSError as e:
        print(f"OSError: {e}")
        print("No default input device available. Check your microphone settings.")
        return None