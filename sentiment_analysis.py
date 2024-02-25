"""Module making a request for providing sentiment response."""
import json
import requests


def sentiment_analyzer(text_to_analyse):
    """Function making a reqest."""
    # pylint: disable=line-too-long
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header,timeout=10)
    if response.status.code == 200:
        formatted_response = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
        return {"label":label,"score":score}
    if response.status.code == 500 :
        return {"label":None,"score":None}
    return None
