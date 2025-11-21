from flask import Flask, render_template, request
from EmotionDetection import emotion_detection   # module

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("textToAnalyze")

    if not text:
        return "Error: No text found in request", 400

    # Run emotion detector
    result_dict = emotion_detection.emotion_detector(text)
        
    # Extract values
    anger_score = result_dict.get("anger")
    disgust_score = result_dict.get("disgust")
    fear_score = result_dict.get("fear")
    joy_score = result_dict.get("joy")
    sadness_score = result_dict.get("sadness")
    dominant_emotion = result_dict.get("dominant_emotion")

    if dominant_emotion == None:
        return "Invalid text! Please try again!"

    # Final response
    result = (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
