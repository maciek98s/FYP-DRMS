from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import numpy as np
import cv2
from werkzeug.utils import secure_filename
import os


def HelloWorld():
    return "cormac is gay"

