# Rasa Lite
RasaLite is a simple and straight forward implementation of Chatbot using Rasa framework.

## Features
- No Need of Story file, Domain file
- Single response.yml file to map intents and utterances
- Independent of Rasa Core

## Dependencies
- This project calls Rasa NLU API so it is necessary to run your trained rasa model as server using below command:
```sh
   rasa run --enable-api 
```

## Installation
1. Install dependencies using ``` pip3 install -r requirements.txt ``` command.
2. Update `response.yml` file with your intents and utterances.

## Run
- Start API using ``` python3 main.py ```

## Test
```sh
curl --location --request POST 'http://localhost:8000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"text":"Hello"}' 
```