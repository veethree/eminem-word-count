from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    with open("static/eminem_word_list.json", "r") as f:
        word_list = json.load(f)

    sorted_list = sorted(word_list.items(), key=lambda x: x[1], reverse=True)
    top_list = {}
    for key,val in enumerate(sorted_list):
        top_list[key] = val
        if len(top_list) > 99:
            break

    if "word" in request.form:
        word = request.form.get("word").strip().lower()
        
        if word in word_list:
            word_count = word_list[word]
        else:
            word_count = 0

        return render_template("index.html", word=word, word_count=word_count, top_list=top_list)
    else:
        return render_template("index.html", top_list=top_list)

@app.route("/top")
def top():
    with open("static/eminem_word_list.json", "r") as f:
        word_list = json.load(f)

    sorted_list = sorted(word_list.items(), key=lambda x: x[1], reverse=True)
    top_list = {}
    for key,val in enumerate(sorted_list):
        top_list[key] = val
        if len(top_list) > 99:
            break

    return render_template("top100.html", top_list=top_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
