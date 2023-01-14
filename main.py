from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from random import choice

app = Flask(__name__)
api = Api(app)

word_post_args = reqparse.RequestParser()
word_post_args.add_argument("german_word", type=str, help="new word in German required", required=True)
word_post_args.add_argument("english_word", type=str, help="new word in English required", required=True)

word_delete_args = reqparse.RequestParser()
word_delete_args.add_argument("german_word", type=str, help="german word requred to delete", required=True)

words = {"furniture": {"der Tisch": "table", "der Stuhl": "chair", "das Regal": "shelves", "das Sofa": "sofa", "das Bett": "bed"}, "vegetables": {"die Kartoffel": "potato", "die Paprika": "(bell) pepper", "die Karotte": "carrot", "die Zwiebel": "onion"}}

def create_category_if_nonexistent(category):
    if not category in words:
        words[category] = {}

def abort_if_category_doesnt_exist(category):
    if not category in words:
        abort(404, message="Couldn't find category...")

def abort_if_word_doesnt_exist(category, german_word):
    if not german_word in words[category]:
        abort(404, message="Couldn't find word...")

class GermanWords(Resource):
    def get(self, category): 
        # returns a random word from the chosen category
        return {"todays word": choice(list(words[category].items()))}

    def post(self, category): 
        args = word_post_args.parse_args()
        create_category_if_nonexistent(category)
        # Adding word to our dictionary
        words[category][args["german_word"]] = args["english_word"]
        print(words)
        return {"added word": args}, 201

    def delete(self, category):
        args = word_delete_args.parse_args()
        abort_if_category_doesnt_exist(category)
        abort_if_word_doesnt_exist(category, args["german_word"])
        del words[category][args["german_word"]]
        print(words)
        return "word deleted", 204


api.add_resource(GermanWords, "/word/<string:category>")

if __name__ == "__main__":
    app.run(debug=True)