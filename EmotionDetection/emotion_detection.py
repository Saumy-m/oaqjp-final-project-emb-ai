''' The funtion in this file detects emotions conveyed by the input text'''
#import required libraries
import requests, json

#define function to detect emotion
def emotion_detector(text_to_analyze):
    #url of api
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #header of api
    header ={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #input type declaration
    inputs= {"raw_document": { "text": text_to_analyze }}

    #response from the api
    resp= requests.post(url, json= inputs, headers= header)
    # anger score from response
    anger_score = json.loads(resp.text)["emotionPredictions"][0]["emotion"]["anger"]
    # disgust score from response
    disgust_score = json.loads(resp.text)["emotionPredictions"][0]["emotion"]["disgust"]
    # fear score from response
    fear_score = json.loads(resp.text )["emotionPredictions" ][0]["emotion" ][ "fear" ]
    # joy score from response
    joy_score = json.loads(resp.text)["emotionPredictions"][0]["emotion"]["joy"]
    # sadness score from response
    sadness_score = json.loads(resp.text)["emotionPredictions"][0]["emotion"]["sadness"]
    # dictionary to find key of highest value
    max_dict={'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    # string to hold the dominant emotion value
    dominant_emotion= max(max_dict, key = max_dict.get)
    # final formatted response
    format_resp= {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}
    return format_resp
