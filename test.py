import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "word/furniture")
print(response.json())

response = requests.get(BASE + "word/furniture")
print(response.json())

response = requests.post(BASE + "word/clothes", json={"german": "der Schal", "english": "scarf"})
print(response.json())

response = requests.post(BASE + "word/clothes", json={"german": "die Hose", "english": "trousers"})
print(response.json())