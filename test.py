import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "get-word/furniture")
print(response.json())

response = requests.post(BASE + "add-word", "name=bob")
print(response.json())