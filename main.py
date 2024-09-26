from flask import Flask, render_template, flash, request 
from app import summarize_youtube_video

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")
        if youtube_url:
            summary = summarize_youtube_video(youtube_url)
    
    return render_template("index.html", summary=summary)


if __name__ == "__main__":
    app.run(debug=True)
