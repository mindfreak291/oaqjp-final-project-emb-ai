"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyzes the emotion of the given text using the emotion_detector function
    and returns a formatted response string.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    # Error handling for blank input
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the index page of the Emotion Detector application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
