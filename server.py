from flask import Flask, render_template, request
import json
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/EmotionDetection", methods=["GET"])
def emotion_detection():
    text = request.args.get("textToAnalyze", "")

    # Run your emotion detection function
    result_dict = emotion_detection.emotion_detector(text)

    # Return the result
    return result_dict

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
