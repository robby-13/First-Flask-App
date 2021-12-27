from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"robby": {"age": 23, "gender": "male"},
        "tim": {"age": 70, "gender": "male"}}

class HelloWorld(Resource):
    # Resource variable allows for certain methods to be used
    # which allow for the program to handle get/post/delete requests
    def get(self, name):
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
