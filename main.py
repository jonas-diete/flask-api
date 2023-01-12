from flask import Flask, request
from flask_restful import Api, Resource
from random import choice

app = Flask(__name__)
api = Api(app)

words = {"furniture": {"der Tisch": "table", "der Stuhl": "chair", "das Regal": "shelves", "das Sofa": "sofa", "das Bett": "bed"}, "vegetables": {"die Kartoffel": "potato", "die Paprika": "(bell) pepper", "die Karotte": "carrot", "die Zwiebel": "onion"}}

class GermanWords(Resource):
    def get(self, category):
        return {"todays word": choice(list(words[category].items()))}

class GermanWordsAdd(Resource):
    def post(self):
        print(request.form["german"])
        return "New word added!"

api.add_resource(GermanWords, "/get-word/<string:category>")
api.add_resource(GermanWordsAdd, "/add-word")

if __name__ == "__main__":
    app.run(debug=True)