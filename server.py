from flask import Flask, request, jsonify
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    statement = data.get('statement', '')

    result = emotion_detection.emotion_detector(statement)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)