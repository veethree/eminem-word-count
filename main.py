from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if "word" in request.form:
        word = request.form.get("word").strip()
        with open("static/eminem_word_list.json", "r") as f:
            word_list = json.load(f)

        if word in word_list:
            word_count = word_list[word]
        else:
            word_count = 0

        return render_template("index.html", word=word, word_count=word_count)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
