import yaml
import random
import requests
from flask import Flask
from flask import request
import json

app = Flask(__name__)

class IntentResponder:
    def __init__(self, response_file="response.yml"):
        with open(response_file, "r") as stream:
            try:
                response = yaml.safe_load(stream)
                self.intent_map = response["responses"]
            except yaml.YAMLError as exc:
                print(exc)
                self.intent_map = {}        

    ''' Return utterance for intent as specified in yml file.'''
    def get_utterence(self, intent):
        if intent in self.intent_map.keys():
            utterences = self.intent_map[intent]
            response = utterences[random.randint(0,len(utterences)-1)]
            return response
        else:
            return "Invalid Intent Name."

intent_responder = IntentResponder()

@app.route("/", methods=["POST"])
def hello_world():
    rasa_api_url = "http://localhost:5005/model/parse"
    params = json.dumps(request.json)
    headers = {'Content-Type': 'application/json'}

    api_response = requests.request("POST", rasa_api_url, headers=headers, data=params)
    pred_result = json.loads(api_response.text)
    utterence = intent_responder.get_utterence(pred_result["intent"]["name"])
    pred_result["response"] = utterence
    del pred_result["response_selector"]

    return json.dumps(pred_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=False)
