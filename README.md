# 📌 AI Voice Assistant using Python

🚀 A smart AI-powered voice assistant built using Python that can respond to voice commands, open applications, fetch weather updates, answer general queries, and much more!

![AI Voice Assistant](https://github.com/user-attachments/assets/912e3dc0-49f8-475a-afe4-3339a06515d1)

---

## 🔍 Features
✅ **Speech Recognition** – Understands and processes voice commands.  
✅ **Text-to-Speech (TTS)** – Converts responses into speech output.  
✅ **Task Automation** – Opens applications, searches Google, plays music, etc.  
✅ **Wikipedia Integration** – Fetches information from Wikipedia.  
✅ **Weather Updates** – Provides real-time weather information.  
✅ **News Headlines** – Reads out the latest news.  
✅ **Smart Reminders** – Sets reminders based on voice input.  
✅ **GUI (Optional)** – A graphical interface for easier interaction.  

---

## 🛠️ Tech Stack
**Programming Language:** Python 🐍  

### **Libraries Used:**
- `SpeechRecognition` → Converts voice to text  
- `pyttsx3` → Converts text to speech  
- `wikipedia` → Fetches information from Wikipedia  
- `pywhatkit` → Plays YouTube videos and performs searches  
- `datetime` → Retrieves date and time  
- `os` → Opens applications  
- `requests` → Fetches weather and news updates  
- `Tkinter (Optional)` → GUI interface  

---

## 📦 Installation

### 1️⃣ Prerequisites
Ensure you have **Python 3.8+** installed on your system.  
🔗 [Download Python](https://www.python.org/downloads/)

### 2️⃣ Install Dependencies
Run the following commands in your terminal or command prompt:
```bash
pip install speechrecognition pyttsx3 wikipedia pywhatkit requests
pip install pyaudio pillow openai
```
⚠ **Note:** If `pyaudio` installation fails, use:
```bash
pip install pipwin 
pipwin install pyaudio
```

### 3️⃣ Clone the Repository
```bash
git clone https://github.com/shadab04/AI-Voice-Assistant.git
cd AI-Voice-Assistant
```

### 4️⃣ Run the Program
```bash
python assistant.py
```

### 5️⃣ Sample Voice Commands:
- **"Open Notepad"**  
- **"Search Python on Google"**  
- **"What is the time?"**  
- **"Tell me about Albert Einstein from Wikipedia"**  
- **"Play a song on YouTube"**  

---

## 📜 Project Workflow (DFD)

### Data Flow Diagram (DFD)
![Data Flow Diagram](https://github.com/user-attachments/assets/628e8696-9d0c-4e81-a82e-9fc4831f59f5)

---

## 🛠️ Modules

🔹 **Speech Recognition Module** – Converts voice to text.  
🔹 **Task Execution Module** – Performs operations based on user commands.  
🔹 **NLP (Natural Language Processing)** – Enhances command interpretation.  
🔹 **GUI (Optional)** – User-friendly interface for interaction.  
🔹 **Database for User Preferences** _(Future Enhancement)_ – Saves user preferences for a personalized experience.

---

## 📌 To-Do List
✔ **Basic Voice Assistant Features**  
✔ **Wikipedia Integration**  
✔ **Open Websites & Apps**  
🚧 **Smart Home Integration** _(Upcoming)_  
🚧 **Multi-language Support** _(Upcoming)_  
🚧 **GPT-based Chat Mode** _(Upcoming)_  

---

## 📷 Screenshots

![Screenshot](https://github.com/user-attachments/assets/e5b1369d-51b1-448b-901d-cd177bac96db)

---

## 🙌 Contribution

Want to contribute? Follow these steps:

1. **Fork the Repository**
2. **Create a New Branch**
```bash
git checkout -b feature-branch
```
3. **Commit Your Changes**
```bash
git commit -m "Added a new feature"
```
4. **Push to GitHub**
```bash
git push origin feature-branch
```
5. **Create a Pull Request**

---

## 🔒 Limitations

⚠ **Accent Recognition Issues** – May not always recognize non-standard accents.  
⚠ **Limited Offline Support** – Requires an internet connection for Wikipedia and weather updates.  
⚠ **Privacy Concerns** – AI assistants may process sensitive voice data.

---

## 📜 License

This project is open-source under the **MIT License**.  
Feel free to modify and distribute it.

---

## 💬 Contact

📧 **Email:** shadabkhanasr04@gmail.com  
🔗 **LinkedIn:** [Shadab Khan](https://www.linkedin.com/in/shadab-khan-37b564236/)  
💻 **GitHub:** [shadab04](https://github.com/shadab04)  

⭐ **If you found this project useful, give it a star on GitHub!** 😊
