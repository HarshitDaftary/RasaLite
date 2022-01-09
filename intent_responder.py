import yaml
import random

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
    def get_utterance(self, intent):
        if intent in self.intent_map.keys():
            utterences = self.intent_map[intent]
            response = utterences[random.randint(0,len(utterences)-1)]
            return response
        else:
            return "Invalid Intent Name."