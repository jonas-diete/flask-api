from flask import Flask
from flask_restful import Api, Resource
from random import choice

app = Flask(__name__)
api = Api(app)

words = {"furniture": ["der Tisch", "der Stuhl", "das Regal", "das Sofa", "das Bett"], "vegetables": ["die Kartoffel", "die Paprika", "die Karotte", "die Zwiebel"]}

class HelloWorld(Resource):
    def get(self, category):
        return {"todays word": choice(words[category])}

api.add_resource(HelloWorld, "/get-word/<string:category>")

if __name__ == "__main__":
    app.run(debug=True)