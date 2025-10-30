''' The funtion in this file detects emotions conveyed by the input text'''
#import required libraries
import requests

#define function to detect emotion
def emotion_detector(text_to_analyze):
    #url of api
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #header of api
    header ={{"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #input type declaration
    inputs= {"raw_document": { "text": text_to_analyze }}

    #response from the api
    resp= requests.post(url, json= inputs, headers= header)
    # return output in text format
    return resp. text