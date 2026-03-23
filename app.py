from flask import Flask, request, send_file
from gtts import gTTS
import tempfile

app = Flask(__name__)

@app.route("/api/tts")
def tts():
    text = request.args.get("text")

    if not text:
        return "Text required", 400

    tts = gTTS(text=text, lang='en')

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)

    return send_file(temp_file.name, as_attachment=True, download_name="voice.mp3")
