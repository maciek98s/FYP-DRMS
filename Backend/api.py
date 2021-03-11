from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import numpy as np
import cv2
from werkzeug.utils import secure_filename
from waitress import serve
import os
import teststests

app = Flask(__name__)
api = Api(app)
CORS(app)

class HelloWorld(Resource):
    def post(self):
        image = request.files["file"]
        print(teststests.HelloWorld())
        print(image)
        filename = secure_filename(image.filename)
        image.save(os.path.join('C:/Users/Maciek/Documents/FYP/Backend', filename))
        return {'hello': 'worldsss'}
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    #context = ('localhost+2.pem', 'localhost+2-key.pem')#certificate and key files
    app.run(host='localhost')