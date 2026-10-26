oaqjp-final-project-emb-ai

Final Project

Emotion Detector web application built with the Watson NLP library and Flask.

Overview

This project is an AI-based web application that analyses a piece of text and detects the emotions it expresses. It sends the text to the Watson NLP EmotionPredict service and reports scores for five emotions (anger, disgust, fear, joy, sadness) together with the dominant emotion.

Features
Emotion detection using the Watson NLP library
Formatted output: a dictionary of the five emotion scores plus dominant_emotion
Packaged as a Python package (EmotionDetection)
Unit tests for the five emotions
Flask web interface
Error handling for blank or invalid input (status code 400)
Static code analysis with pylint (score 10/10)
Project Structure
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py              # Package initialiser, imports emotion_detector
│   └── emotion_detection.py     # Emotion detection function
├── static/
│   └── mywebscript.js           # Front-end script (calls the Flask route)
├── templates/
│   └── index.html               # Web page
├── emotion_detection.py         # Standalone copy of the function (Tasks 2-3)
├── server.py                    # Flask application
├── test_emotion_detection.py    # Unit tests
├── requirements.txt             # Python dependencies
└── README.md
Installation
bash
git clone https://github.com/bhapkarkirti213-stack/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
pip install -r requirements.txt
Usage
Use the function directly
python
from EmotionDetection.emotion_detection import emotion_detector

print(emotion_detector("I am very angry"))

Example output:

{'anger': 0.99, 'disgust': 0.01, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0, 'dominant_emotion': 'anger'}

(Scores shown are illustrative; real values come from the Watson service.)

Run the web application
bash
python3 server.py

Open http://localhost:5000, enter some text and click Run Emotion Detection.

Example response:

For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002,
'fear': 0.009, 'joy': 0.97 and 'sadness': 0.013. The dominant emotion is joy.
Error Handling

If the input is blank, Watson returns status code 400. emotion_detector then returns None for every key, and the server responds with:

Invalid text! Please try again!
Unit Tests
bash
python3 test_emotion_detection.py
Statement	Expected dominant emotion
I am glad this happened	joy
I am really mad about this	anger
I feel disgusted just hearing about this	disgust
I am so sad about this	sadness
I am really afraid that this will happen	fear
Static Code Analysis
bash
pylint server.py

Result: 10.00/10.

Tasks Completed
Cloned/forked the project repository
Created the emotion detection application with the Watson NLP library
Formatted the application output
Packaged the application (EmotionDetection)
Ran unit tests
Deployed the application with Flask
Incorporated error handling
Ran static code analysis
Technologies

Python 3, Flask, Requests, Watson NLP (EmotionPredict), unittest, pylint
