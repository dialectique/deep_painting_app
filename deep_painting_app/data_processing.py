
import random
import numpy as np
from tensorflow.keras.preprocessing import image_dataset_from_directory

def load_and_divide_dataset(path="", validation_split=0.2, batch_size=1, img_height=180, img_width=180):
    """
    Charge the dataset from the specified path (by default: current path)
    The database must be divided into folders (one folder per class).
    Return a tuple od two datasets:
    * dataset_train
    * dataset_validation
    -> both are type: tensorflow.python.data.ops.dataset_ops.BatchDataset
    batch_size is the number of element per batch. By default: 1
    image size: img_height and img_width. By default 180 for both
    validation_split: fraction of data to reserve for validation. Bydefault 0.2
    """

    # raise an error if batch_size is not a positive interger
    if not type(batch_size) is int or batch_size < 0:
        raise TypeError("batch_size must be a positive integer")

    # raise an error if path is not a string
    if not type(path) is str:
        raise TypeError("path must be a string")

    # raise an error if validation_split is not not a float between 0 and 1
    if not type(validation_split) is float or validation_split > 1 or validation_split < 0:
        raise TypeError("validation_split must be a float between 0 and 1")

    #raise an error if img_height is not a positive int
    if not type(img_height) is int or img_height <= 0:
        raise TypeError("img_height must be a positive integer")

    #raise an error if img_width is not a positive int
    if not type(img_width) is int or img_width <= 0:
        raise TypeError("img_width must be a positive integer")

    random.seed()
    seed = random.randint(0,100)

    dataset_train = image_dataset_from_directory(
        path,
        validation_split = validation_split,
        labels='inferred',
        subset='training',
        label_mode='categorical',
        shuffle = True,
        seed = seed,
        image_size = (img_height, img_width),
        color_mode='rgb',
        batch_size=batch_size)

    dataset_validation = image_dataset_from_directory(
        path,
        validation_split = validation_split,
        labels='inferred',
        subset='validation',
        label_mode='categorical',
        shuffle = True,
        seed = seed,
        image_size = (img_height, img_width),
        color_mode='rgb',
        batch_size=batch_size)

    return dataset_train, dataset_validation


def classes_names_to_dict(dataset):
    """
    return a dict of the classes and corresponding vectors
    dataset type: tensorflow.python.data.ops.dataset_ops.BatchDataset
    https://www.tensorflow.org/jvm/api_docs/java/org/tensorflow/op/data/BatchDataset
    """

    # raise an error if dataset is not a tensorflow BatchDataset
    if not dataset.__class__.__name__ == 'BatchDataset':
        raise TypeError("This function has been written for tensorflow BatchDataset\n\
           Please check https://www.tensorflow.org/jvm/api_docs/java/org/tensorflow/op/data/BatchDataset")

    classes_names = dataset.class_names
    identity_matrix = np.identity(len(classes_names)).tolist()

    classes_dict = dict(zip(classes_names, identity_matrix))
    return classes_dict


def give_class_name(vector, class_names_dict):
    """
    return the artistic movement given the associated vector in class_names_dict
    vector can be a list ou a np.array
    class_names_dict should be set with the classes_names_to_dict from this file librairy
    """
    for class_name, v in class_names_dict.items():
        if v == list(vector):
            return class_name


if __name__ == '__main__':
    path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    img_height=180
    img_width=180
    batch_size=1
    validation_split=0.2
    train_ds, test_ds = load_and_divide_dataset(
        path=path,
        img_height=img_height,
        img_width=img_width,
        batch_size=batch_size,
        validation_split=validation_split)
    class_names_dict = classes_names_to_dict(train_ds)
    print(class_names_dict)
