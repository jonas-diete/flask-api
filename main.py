from flask import Flask
from flask_restful import Api, Resource, reqparse
from random import choice

app = Flask(__name__)
api = Api(app)

word_post_args = reqparse.RequestParser()
word_post_args.add_argument("german", type=str, help="new word in German required", required=True)
word_post_args.add_argument("english", type=str, help="new word in English required", required=True)

words = {"furniture": {"der Tisch": "table", "der Stuhl": "chair", "das Regal": "shelves", "das Sofa": "sofa", "das Bett": "bed"}, "vegetables": {"die Kartoffel": "potato", "die Paprika": "(bell) pepper", "die Karotte": "carrot", "die Zwiebel": "onion"}}

def create_category_if_not_existing(category):
    if not category in words:
        words[category] = {}

class GermanWords(Resource):
    def get(self, category):
        # returns a random word from the chosen category
        return {"todays word": choice(list(words[category].items()))}

    def post(self, category):
        args = word_post_args.parse_args()
        create_category_if_not_existing(category)
        # Adding word to our dictionary
        words[category][args["german"]] = args["english"]
        print(words)
        return {"added word": args}, 201

api.add_resource(GermanWords, "/word/<string:category>")

if __name__ == "__main__":
    app.run(debug=True)