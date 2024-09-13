import openai
import text_to_speech

##Set your OpenAI API key here
openai.api_key = ''

# Flag to track whether the AI response has been spoken
response_spoken = False

def get_ai_response(query):
    global response_spoken
    try:
        if not response_spoken:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=query,
                max_tokens=50
            )
            ai_response = response.choices[0].text.strip()
            text_to_speech.speak_text(ai_response)  # Speak the AI response
            response_spoken = '1'  # Set the flag to True after speaking once
            return ai_response
        else:
            return "AI response already spoken"

    except Exception as e:
        print(f"Error in OpenAI query: {e}")
        return "Error in OpenAI query"
