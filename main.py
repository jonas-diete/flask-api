from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from random import choice

app = Flask(__name__)
api = Api(app)

word_post_args = reqparse.RequestParser()
word_post_args.add_argument("category", type=str, help="category of new word required", required=True)
word_post_args.add_argument("german", type=str, help="new word in German required", required=True)
word_post_args.add_argument("english", type=str, help="new word in English required", required=True)

words = {"furniture": {"der Tisch": "table", "der Stuhl": "chair", "das Regal": "shelves", "das Sofa": "sofa", "das Bett": "bed"}, "vegetables": {"die Kartoffel": "potato", "die Paprika": "(bell) pepper", "die Karotte": "carrot", "die Zwiebel": "onion"}}

class GermanWords(Resource):
    def get(self, category):
        return {"todays word": choice(list(words[category].items()))}

class GermanWordsAdd(Resource):
    def post(self):
        args = word_post_args.parse_args()
        return {"added word": args}

api.add_resource(GermanWords, "/get-word/<string:category>")
api.add_resource(GermanWordsAdd, "/add-word")

if __name__ == "__main__":
    app.run(debug=True)