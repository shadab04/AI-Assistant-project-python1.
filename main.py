from tkinter import *
from PIL import ImageTk, Image
import speech_to_text
import text_to_speech
import action
# Define the speak_text function
def speak_text(text):
    engine = text_to_speech.pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in text-to-speech: {e}")

def Ask():
    user_data = speech_to_text.speech_to_text()
    bot_value = action.action(user_data)
    text.insert(END, 'User ---> ' + user_data + "\n")
    if bot_value is not None:
        text.insert(END, "Bot <--- " + bot_value + "\n")
        text_to_speech.speak_text(bot_value)
        if bot_value.lower() == "ok sir":
            root.destroy()
def send():
    sent = entry.get()
    bot = action.action(sent)
    text.insert(END, 'User ---> ' + sent + "\n")
    if bot is not None:
        text.insert(END, "Bot <--- " + bot + "\n")
        speak_text(bot)  # Speak the bot's response
        if bot.lower() == "ok sir":
            root.destroy()

def delete():
    text.delete('1.0', END)

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3)
frame.config(bg="#6F8FAF", relief="raised")
frame.grid(row=0, column=1, padx=55, pady=10)

# Load and resize the image
image_path = "C:\\Users\\DELL\\OneDrive\Desktop\\jarvis.jpeg"
original_image = Image.open( "C:\\Users\\DELL\\OneDrive\Desktop\\jarvis.jpeg")
resized_image = original_image.resize((300, 300))
image = ImageTk.PhotoImage(resized_image)

# Image Label
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# Text Widget
text = Text(root, font=('courier 10 bold'), bg="#356696")
text.place(x=100, y=375, width=375, height=100)

# Entry Widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

# Button 1
button1 = Button(root, text="Ask", bg="#356696", pady=16, padx=40, bd=3, relief=SOLID, command=Ask)
button1.place(x=100, y=550, width=100, height=30)

button2 = Button(root, text="Delete", bg="#356696", pady=16, padx=40, bd=3, relief=SOLID, command=delete)
button2.place(x=220, y=550, width=100, height=30)

button3 = Button(root, text="Send", bg="#356696", pady=16, padx=40, bd=3, relief=SOLID, command=send)
button3.place(x=340, y=550, width=100, height=30)

# Start the main event loop
root.mainloop()












