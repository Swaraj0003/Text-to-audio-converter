Text-to-Speech Web Application

A simple and user-friendly web application that converts user-entered text into natural-sounding speech using Google Text-to-Speech (gTTS). The application is built using Python, Flask, HTML, and CSS.

 Features

Convert text to speech in real time

Supports multiple languages (English, Hindi, Malayalam, Tamil, French, etc.)

Web-based interface — no installation required for end users

Audio playback directly in the browser

Lightweight and easy to deploy


Tech Stack

Component	Technology

Backend     	        Python, Flask
Frontend     	        HTML, CSS
Text to Speech      	gTTS (Google Text-to-Speech)
Audio Format	        MP3


text-to-speech/

│
├── app.py

├── requirements.txt

├── static/

│   └── style.css

└── templates/

    └── index.html

'''

git clone https://github.com/your-username/text-to-speech.git

cd text-to-speech
'''


pip install -r requirements.txt



python app.py


 Limitations

Requires an active internet connection (gTTS uses Google’s online API).

Audio generation speed depends on network quality.

