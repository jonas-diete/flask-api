import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "get-word/furniture")
print(response.json())

response = requests.post(BASE + "add-word", json={"category": "clothes", "german": "die Hose", "english": "trousers"})
print(response.json())