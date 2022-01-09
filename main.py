import requests
from flask import Flask
from flask import request
import json
from intent_responder import IntentResponder

app = Flask(__name__)

intent_responder = IntentResponder()

@app.route("/predict", methods=["POST"])
def predict():
    rasa_api_url = "http://localhost:5005/model/parse"
    params = json.dumps(request.json)
    headers = {'Content-Type': 'application/json'}

    api_response = requests.request("POST", rasa_api_url, headers=headers, data=params)
    pred_result = json.loads(api_response.text)
    utterance = intent_responder.get_utterance(pred_result["intent"]["name"])
    pred_result["response"] = utterance
    del pred_result["response_selector"]

    return json.dumps(pred_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=False)
