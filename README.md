# 🤖 JARVIS AI - Personal Voice Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/Version-1.0-orange)

An intelligent voice-controlled personal assistant built with Python. JARVIS can recognize voice commands, speak responses, fetch real-time information, control your browser, play music, and answer questions using Google's Gemini AI.

---

# ✨ Features

### 🎤 Voice Recognition

* Wake word detection ("Jarvis")
* Speech-to-text using Google Speech Recognition
* Natural voice interaction

### 🔊 Text-to-Speech

* Speaks responses naturally
* Voice feedback for every command

### 🌐 Web Automation

* Open Google
* Open YouTube
* Open Facebook
* Open LinkedIn

### 🎵 Music Player

* Play songs from your personal music library

### 📰 Latest News

* Fetches and reads the latest news headlines

### 🌤️ Weather

* Provides live weather updates
* Temperature
* Weather description

### 🕒 Time & Date

* Current time
* Current date

### 🤖 Gemini AI Integration

* Ask any question
* AI-powered conversations
* General knowledge
* Coding assistance
* Educational support

### 🔐 Secure API Keys

* Uses `.env` file
* API keys are never stored in source code

---

# 🛠️ Technologies Used

* Python 3.11
* SpeechRecognition
* PyAudio
* pyttsx3
* Google Gemini API
* OpenWeatherMap API
* NewsAPI
* Requests
* python-dotenv
* Webbrowser

---

# 📂 Project Structure

```text
JARVIS AI/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
│
├── main.py
├── gemini.py
├── MusicLibrary.py
├── test_gemini.py
│
└── .venv/
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/your-username/JARVIS-AI.git
cd JARVIS-AI
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Keys

Create a file named

```text
.env
```

Add:

```env
NEWS_API_KEY=YOUR_NEWS_API_KEY
WEATHER_API_KEY=YOUR_WEATHER_API_KEY
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🎙️ Example Voice Commands

## Browser

* Jarvis open Google
* Jarvis open YouTube
* Jarvis open Facebook
* Jarvis open LinkedIn

## Music

* Jarvis play believer

## Weather

* Jarvis weather

## News

* Jarvis news

## Time

* Jarvis what is the time

## Date

* Jarvis what is today's date

## AI

* Jarvis who is Elon Musk

* Jarvis explain quantum computing

* Jarvis write Python code for a linked list

---


# 📦 Future Features

* Desktop GUI
* WhatsApp Automation
* Email Assistant
* Open Installed Applications
* Screenshot Capture
* Camera Integration
* Face Recognition
* PDF Reader
* Browser Automation
* Calendar Integration
* Reminder System
* Conversation Memory
* Smart Home Control
* Offline Speech Recognition
* AI Agent Automation

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Naveen Kumar Veeramsetty**

B.Tech Computer Science Engineering

GitHub: https://github.com/NaveenRoyallll

---

## ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.

It motivates me to build more AI projects.
