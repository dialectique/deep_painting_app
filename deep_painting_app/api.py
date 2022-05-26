"""
This lib must be used with a API from FastAPI
"""

import numpy as np
import io
from fastapi import UploadFile, File
from PIL import Image
from tensorflow.keras.models import load_model

def index():
    """
    Define a root '/' endpoint. Return a dict with a greeting
    Should be used with the decorator: @app.get("/") where app is the API
    """
    return dict(greeting="Welcome to the Deep Painting App API!!")


def predict_movement(model_path, input_image):
    """
    Return a dict with a predicted artistic movement of the input_image
    This function is used in the 'predict' function from this library
    Arguments:
    * model_path : path of the model
    * input_image: image - jpg

    """
    model = load_model(model_path)
    image = Image.open(io.BytesIO(input_image))
    np_image = np.expand_dims(np.array(image), axis=0)
    prediction = model.predict(np_image)
    return prediction


async def predict(model_path, file: UploadFile = File(...)):
    """
    Define a predict endpoint
    Return a dict of the predicted artistic movement of the input_image(file)
    Arguments:
    * model_path : path of the model
    * file: image - jpg
    Should be used with the decorator: @app.post("/predict") where app is the API
    This function need the 'predict_movement' function from this librairy
    """
    return predict_movement(file, model_path)



if __name__ == '__main__':
    print("to do")
