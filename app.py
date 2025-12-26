from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form.get("lang", "en")

        filename = f"speech_{uuid.uuid4()}.mp3"
        filepath = os.path.join("static", filename)

        tts = gTTS(text=text, lang=lang)
        tts.save(filepath)

        return render_template("index.html", audio_file=filename)

    return render_template("index.html", audio_file=None)

if __name__ == "__main__":
    app.run(debug=True)
