# Rasa Lite

Rasa Lite is a simple and straight forward implementation of Chatbot using Rasa framework. I feel Rasa Core unnecessarily **predicts utterances** and demands for **domains** and **story** files. To know more about this project, checkout my blog on  [Rethinking Rasa Chatbot](https://daftaryharshit.medium.com/rethinking-rasa-chat-bot-f465e64051bd)

Rasa Lite follows rule based approach to return utterance. You can specify your Intent - Utterances mapping in single `YAML` file

## Features

- No need of Story file, Domain file etc.
- Single `response.yml` file to map intents and utterances
- Independent of **RASA Core**

## Dependencies

This project calls Rasa NLU API so it is necessary to run your trained rasa model as server using below command:

```sh
   rasa run --enable-api 
```

## Installation

1. Install dependencies using ``` pip install -r requirements.txt ``` command.
2. Update `response.yml` file with your intents and utterances.

```yaml
responses:
  greet:
    - "Hey! How are you?"
    - "what about you? How are you?"
  goodbye:
    - "Bye have a nice day"
```

## Run

Start API using ``` python main.py ```

## Test

```sh
curl --location --request POST 'http://localhost:8000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"text":"Hello"}' 
```
