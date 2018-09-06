import flask
import numpy as np
import io
from PIL import Image
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils

app = flask.Flask(__name__)
app.config['DEBUG'] = True

model = None

def load_model():
    # loading keras model pre trained on imagenet
    global model
    model = ResNet50(weights='imagenet')

def prepare_to_model():
    pass

def predict():
    pass
