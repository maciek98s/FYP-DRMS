#-------------------------------------------------------------------------------------------------------------------------------------------
'''
Author: Maciej Skrzypczynski
Data: 06/04/2021
Description: This program is the API program. THe API is hosted through this file. The Post request accepts an image and saved the 
image to the backend directory. After the file is saved the program imports the processing.py file and uses its functions 
to return a result which contains the prediction of diabetic retinopathy based on the image the programm has previously saved
'''
#-------------------------------------------------------------------------------------------------------------------------------------------
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import numpy as np
import cv2
from werkzeug.utils import secure_filename
from waitress import serve
import os
import Processing
#-------------------------------------------------------------------------------------------------------------------------------------------

#initializing the API
app = Flask(__name__)
api = Api(app)
CORS(app)

#Class contain POST and GET requests 
class predictionAPI(Resource):
    def post(self):
        image = request.files["file"]
        image.filename = "test.jpg"
        print(image)
        
        filename = secure_filename(image.filename)
        image.save(os.path.join('C:/Users/Maciek/Documents/Github/FYP/FYP/Backend/userImage', filename))
        result = "null"
        result = Processing.predictResult()
        ret = result.astype(str)
        print(ret)
        return ret
    def get(self):
        return {'hello': 'world'}

api.add_resource(predictionAPI, '/')

#lauchinh the API 
if __name__ == '__main__':
    #context = ('localhost+2.pem', 'localhost+2-key.pem')#certificate and key files
    app.run(host='localhost')
#-------------------------------------------------------------------------------------------------------------------------------------------