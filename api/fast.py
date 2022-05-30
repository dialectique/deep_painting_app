#!/usr/bin/env python
"""
API for the Deep Painting App
"""

__author__ = 'Bryan Battenfelder'
__version__ = '1.0.3'
__status__ = 'Development'


from distutils import extension
from imp import load_module
from urllib import response


from tensorflow.keras.models import load_model
import numpy as np
import io
import shutil
import pytz

import pandas as pd
import joblib

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from PIL import Image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    )

@app.get("/")
def index():
    return dict(greeting="Welcome to the Deep Painting App API!!")


def read_imagefile(file) -> Image.Image:
    """load an image file to be used in the prediction
    """
    image = Image.open(io.BytesIO(file))
    return image

def load_in_model():
    """load in a model to be used in the prediction
    """
    return load_model('./models/my_model')

model = load_in_model()

image_movement_dict = {
    0:'Northern Renaissance',
    1:'Ukiyo-e',
    2:'High Renaissance',
    3:'Impressionism',
    4:'Post Impressionism',
    5:'Rococo'
    }

def predict_image_class(image: Image.Image):
    """predicts the image class
    """
    image = np.asarray(image.resize((224, 224)))[...,:3]
    np_image = np.expand_dims(image,0)
    np_image = np_image #/ 127.5 -1
    result = model.predict(np_image)[0]
    movement = np.argmax(result)
    #response = []
    resp = {}
    resp['movement'] = image_movement_dict[int(movement)]
    resp['confidence'] = float(result[int(movement)])
    #response.append(resp)
    print(resp)
    return resp




@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    #image = read_imagefile(file)
    image = read_imagefile(await file.read())
    prediction = predict_image_class(image)

    return prediction


    # ⚠️ TODO: get model from GCP

    # # pipeline = get_model_from_gcp()
    # pipeline = joblib.load('model.joblib')

    # # make prediction
    # results = pipeline.predict(X)

    # # convert response from numpy to python type
    # pred = float(results[0])

    # return dict(fare=pred)
