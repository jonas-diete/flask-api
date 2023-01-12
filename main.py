from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)



class HelloWorld(Resource):
    def get(self, category):
        return {"category": category}

    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/get-word/<string:category>")

if __name__ == "__main__":
    app.run(debug=True)