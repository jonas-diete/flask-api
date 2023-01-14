import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "word/furniture")
print(response.json())

response = requests.get(BASE + "word/furniture")
print(response.json())

response = requests.post(BASE + "word/clothes", json={"german_word": "der Schal", "english_word": "scarf"})
print(response.json())

response = requests.post(BASE + "word/clothes", json={"german_word": "die Hose", "english_word": "trousers"})
print(response.json())

response = requests.delete(BASE + "word/furniture", json={"german_word": "das Bett"})
# doesn't print correct response yet - debug
print(response)