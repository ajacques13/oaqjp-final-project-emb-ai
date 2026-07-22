"""
Emotion Detection Flask Server
"""

from flask import Flask
from flask import request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze user input and return emotion analysis.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Render index page.
    """
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
