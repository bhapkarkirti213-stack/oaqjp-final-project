"""Emotion detection using the Watson NLP EmotionPredict service."""
import json

import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.nlp-runtime/NLPService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ['anger', 'disgust', 'fear', 'joy', 'sadness']


def emotion_detector(text_to_analyse):
    """Analyse text and return the five emotion scores and the dominant emotion.

    If the service responds with status code 400 (e.g. blank input), every
    value in the returned dictionary is None.
    """
    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)

    if response.status_code == 400:
        result = {emotion: None for emotion in EMOTIONS}
        result['dominant_emotion'] = None
        return result

    formatted = json.loads(response.text)
    scores = formatted['emotionPredictions'][0]['emotion']
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result['dominant_emotion'] = max(result, key=result.get)
    return result
