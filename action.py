//for action 
import webbrowser
import datetime
import weather
import text_to_speech
import ai_module

def action(user_data):
    user_data = user_data.lower()

    if "what is your name" in user_data:
        return "My name is virtual assistant"

    elif "hello" in user_data or "hey" in user_data:
        return "Hey, sir. How can I help you?"

    elif "good morning" in user_data:
        return "Good morning, sir."

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        time_str = f"Hour: {current_time.hour}, Minute: {current_time.minute}"
        return f"Time now: {time_str}"

    elif "shutdown" in user_data:
        return "OK, sir. Shutting down."

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        return "Gaana.com is now ready for you."

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        return "YouTube.com is now ready for you."

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        return "Google.com is now ready for you."

    elif "weather" in user_data:
        default_location = "delhi"
        ans = weather.get_weather_info(default_location)
        if ans:
            text_to_speech.speak_text(f"Weather in {default_location}: {ans['temperature']}°C, {ans['weather_desc']}")
            return f"Weather in {default_location}: {ans['temperature']}°C, {ans['weather_desc']}"

    elif "using artificial intelligence" in user_data:

        # Extract the relevant part of the query for OpenAI
        ai_query = user_data.replace("using artificial intelligence", "").strip()
        # For other queries, use OpenAI to generate a response
        ai_response = ai_module.get_ai_response(ai_query)
        if ai_response:
            text_to_speech.speak_text(ai_response)
            return ai_response
        else:
            return "Error in generating AI response"

    else:
        return "I'm sorry, I didn't understand that."



