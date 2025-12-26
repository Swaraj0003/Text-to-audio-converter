🔊 Text-to-Speech Web Application

This project is a web-based Text-to-Speech (TTS) application that converts user-entered text into natural-sounding speech using Google Text-to-Speech (gTTS). It is built with Python and Flask on the backend and HTML/CSS on the frontend.

Features

Convert text to speech in real time

Supports multiple languages (English, Hindi, Malayalam, Tamil, French)

Audio playback directly in the browser

Simple and responsive user interface

Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS

Text-to-Speech Engine: gTTS

Audio Format: MP3

Project Structure
text-to-speech/
│
├── app.py
|
├── requirements.txt
|
├── static/
|   |
│   └── style.css
|
└── templates/
|   |
    └── index.html

Installation

git clone https://github.com/your-username/text-to-speech.git
cd text-to-speech
pip install -r requirements.txt
python app.py


Open in browser:

http://127.0.0.1:5000

Usage:

Enter text in the input box.

Select a language.

Click "Convert to Speech".

Listen to the generated audio.





Developed as a learning and demonstration project.
