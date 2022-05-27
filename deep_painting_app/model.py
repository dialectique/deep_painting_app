"""
Deep painting app
Model(s) and pipeline(s)
"""

from tensorflow.keras import layers
from tensorflow.keras import models
from deep_painting_app.data_processing import load_and_divide_dataset, classes_names_to_dict, give_class_name

def initialize_baseline_model(img_height=180, img_width=180):
    """
    set up the baseline model
    return a keras sequential model
    arguments: img_height and img_width for the rescaling layer
    """
    # About the rescaling layer: I have set default values for img_height=180, img_width=180
    # I am not sure if is good or not. Please, modifiy if needed. Gilles

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


def baseline_model_pipeline(path="", validation_split=0.2, batch_size=1, img_height=180, img_width=180):
    """
    return a baseline model pipeline
    arguments:
    path: path of the dataset (by default: current path) - the database must be divided into folders (one folder per class).

    batch_size is the number of element per batch. By default: 1
    image size: img_height and img_width. By default 180 for both
    validation_split: fraction of data to reserve for validation. Bydefault 0.2
    """
    # I am really not sure if this pipeline is the best way to do... Gilles

    train_ds, test_ds = load_and_divide_dataset(
        path=path,
        img_height=img_height,
        img_width=img_width,
        batch_size=batch_size,
        validation_split=validation_split)
    class_names_dict = classes_names_to_dict(train_ds)
    model = initialize_baseline_model(img_height, img_width)

    # add instructions, if not, this pipeline is not usefull.

    return model


if __name__ == '__main__':
    path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    model = baseline_model_pipeline(path)
    print(type(model))
