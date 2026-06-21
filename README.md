🤖 Jarvis AI Assistant

A Python-based voice-controlled AI assistant inspired by Iron Man's JARVIS.

Jarvis can listen to voice commands, open websites, play music, and read the latest news using voice responses.

---

🚀 Features

🎙 Voice Activation

- Wake word detection using:
  - "Jarvis"

🌐 Open Websites

Voice commands:

- Open Google
- Open YouTube
- Open Facebook
- Open LinkedIn

🎵 Music Playback

Play songs directly from a predefined music library.

Example:

- Play Believer
- Play Shape of You

📰 Latest News

Fetches and reads the latest headlines using NewsAPI.

Example:

- News
- Tell me the news
- Latest news

🔊 Text-to-Speech

Jarvis responds using voice output powered by pyttsx3.

🎤 Speech Recognition

Converts spoken commands into text using Google Speech Recognition.

---

🛠 Tech Stack

Language

- Python 3.11+

Libraries

- SpeechRecognition
- PyAudio
- pyttsx3
- Requests
- WebBrowser

APIs

- NewsAPI

---

📂 Project Structure

Jarvis-AI/
│
├── main.py
├── MusicLibrary.py
├── requirements.txt
├── README.md
│
└── assets/

---

⚙️ Installation

1. Clone Repository

git clone https://github.com/yourusername/Jarvis-AI.git

cd Jarvis-AI

2. Create Virtual Environment

python -m venv .venv

3. Activate Environment

Windows:

.venv\Scripts\activate

Linux / Mac:

source .venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

Or

pip install SpeechRecognition
pip install PyAudio
pip install pyttsx3
pip install requests

---

🔑 Configure News API

Get a free API key from:

https://newsapi.org

Replace:

newsapi = "YOUR_API_KEY"

with your API key.

---

🎵 Music Library Setup

Create a file named:

MusicLibrary.py

Example:

music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shapeofyou": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}

---

▶️ Run Project

python main.py

---

🗣 Example Commands

Open Websites

Jarvis
Open Google

Jarvis
Open YouTube

Play Music

Jarvis
Play Believer

Get News

Jarvis
News

---

🔮 Future Enhancements

- AI Chat Integration (OpenAI/Gemini)
- Weather Updates
- WhatsApp Messaging
- Open Desktop Applications
- Screenshots
- File Management
- Email Sending
- Calendar Integration
- Smart Home Control
- Personal Memory System

---

🐞 Known Issues

- Requires internet connection for speech recognition.
- PyAudio installation can be difficult on some Windows systems.
- Background noise may affect recognition accuracy.

---

🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Push changes
5. Create a Pull Request

---

👨‍💻 Author

Naveen Kumar Veeramsetty

B.Tech Computer Science Engineering

Passionate about AI, Full Stack Development, and Building Real-World Projects.

---

⭐ If you like this project, don't forget to star the repository!