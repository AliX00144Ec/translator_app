from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    if request.method == "POST":
        italian_text = request.form["italian_text"]
        if italian_text.strip() != "":
            translated = translator.translate(italian_text, src='it', dest='ar')
            translation = translated.text
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)
