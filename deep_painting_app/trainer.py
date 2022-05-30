#!/usr/bin/env python
"""
Baseline Model to test the Deep Painting App
"""

#from google.cloud import storage



import numpy as np
import pandas as pd

from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.callbacks import EarlyStopping

import joblib


__author__ = 'Bryan Battenfelder'
__version__ = '1.0.0'
__status__ = 'Development'



def get_data(path = "", validation_split = 0.2, batch_size = 10, img_height = 180, img_width = 180):
    """method to get the training data from a directory"""

    train_ds = image_dataset_from_directory(
        path,
        validation_split= 0.2,
        subset='training',
        labels='inferred',
        label_mode='categorical',
        shuffle=True,
        seed = 123,
        image_size = (img_height, img_width),
        color_mode = 'rgb',
        batch_size = batch_size)


    test_ds = image_dataset_from_directory(
        path,
        validation_split = 0.2,
        subset='validation',
        labels='inferred',
        label_mode = 'categorical',
        shuffle = True,
        seed = 123,
        image_size = (img_height, img_width),
        color_mode = 'rgb',
        batch_size = batch_size
        )


    return train_ds, test_ds



# ... Define a model

def initalize_model():
    model = models.Sequential()

    ### Rescaling Layer ###
    model.add(layers.Rescaling(1./255, input_shape = (img_height, img_width, 3))) # check this may need to divide by the image size

    ### First Convolution & Max Pooling ###
    model.add(layers.Conv2D(8, (4,4), activation = 'relu', padding = 'same'))
    model.add(layers.MaxPool2D(pool_size = (2,2)))

    ### Second Convolution & MaxPooling
    model.add(layers.Conv2D(16, (3,3), activation='relu', padding='same'))
    model.add(layers.MaxPool2D(pool_size=(2,2)))

    ### Flattening
    model.add(layers.Flatten())

    ### One Fully Connected layer - "Fully Connected" is equivalent to saying "Dense"
    model.add(layers.Dense(10, activation='relu'))

    ### Last layer - Classification Layer with 6 outputs corresponding to 6 art styles
    model.add(layers.Dense(6, activation='softmax'))

    ### Model compilation
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model

def train_model(train_ds, test_ds, patience = 5, epochs = 10, batch_size = 32):
    es = EarlyStopping(patience=patience)
    epochs = epochs
    batch_size = batch_size

    history = model.fit(train_ds,
                        validation_data = test_ds,
                        epochs = epochs,
                        batch_size = batch_size,
                        callbacks = [es],
                        verbose = 1
                        )
    print("Well Done, Your Model is Now Trained......")
    return history



STORAGE_LOCATION = 'models/deeppainting/model.joblib'


def upload_model_to_gcp():


    client = storage.Client()

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(STORAGE_LOCATION)

    blob.upload_from_filename('model.joblib')


def save_model(model):
    """method that saves the model
    """

    # saving the trained model to disk is mandatory to then beeing able to upload it to storage
    # Implement here
    model.save('./models/my_model')
    print("saved model locally")

    # Implement here
    # upload_model_to_gcp()
    # print(f"uploaded model.joblib to gcp cloud storage under \n => {STORAGE_LOCATION}")


if __name__ == '__main__':
    # get training data from GCP bucket
    train_ds, test_ds = get_data('/media/tokyofixed/DATA/le_wagon_files/dataset/deep_painting_dataset/orgImg_small')
    img_height = 180
    img_width = 180
    model = initalize_model()


    # preprocess data
    #X_train, y_train = preprocess(df)

    # train model (locally if this file was called through the run_locally command
    # or on GCP if it was called through the gcp_submit_training, in which case
    # this package is uploaded to GCP before being executed)
    train_model(train_ds, test_ds)
    #model.save('my_model')
    save_model(model)
