

#Deep painting app
#Explore processing

#display_paintings_and_classes(dataset, n=1)
#random_painting(path, img_height=180, img_width=180)
#number_img_per_class
#pick_up_one_painting_per_class

import os
import math
import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt
#from deep_painting_app.data_processing import load_and_divide_dataset, classes_names_to_dict, give_class_name
#from tensorflow.keras.preprocessing import image_dataset_from_directory


def display_paintings_and_classes(dataset, n=1):
    """
    display n paintings and classes from dataset, in a optimzed square grid
    images must be RGB, floats between 0 and 255
    dataset type: tensorflow.python.data.ops.dataset_ops.BatchDataset
    """

    # total number of paintings
    n_max = dataset.cardinality().numpy()

    # raise an error if dataset is not a tensorflow BatchDataset
    if not dataset.__class__.__name__ == 'BatchDataset':
        raise TypeError("This function has been written for tensorflow BatchDataset\n\
           Please check https://www.tensorflow.org/jvm/api_docs/java/org/tensorflow/op/data/BatchDataset")

    # raise an error if n is not a positive interger
    if not type(n) is int or n <= 0:
        raise TypeError("n must be a positive integer")

    # raise an error if n > max number of paintings
    if n > n_max:
        raise TypeError("n must be less than or equal to the total number of paintings")

    # display paintings
    n_by_row = math.isqrt(n)
    n_rows = math.ceil(n / n_by_row)
    class_names_dict = classes_names_to_dict(dataset)
    figure, axs = plt.subplots(n_rows, n_by_row, figsize=(20,20))
    i=0
    for x, y in dataset.as_numpy_iterator():
        axs[i//n_by_row, i%n_by_row].imshow(x[0]/255)
        axs[i//n_by_row, i%n_by_row].set_title(give_class_name(y[0], class_names_dict))
        axs[i//n_by_row, i%n_by_row].axis('scaled')
        i += 1
        if i > n - 1:
            break
    # remove unused subplots on the last row
    while i < n_rows * n_by_row:
        axs[i//n_by_row, i%n_by_row].set_axis_off()
        i += 1
    figure.tight_layout()
    plt.show()


def number_img_per_class(path):
    """
    return a dictionnary (keys: class - values: number of images)
    argument: path of the dataset
    The database must be divided into folders (one folder per class)
    """
    class_list = os.listdir(path)
    dict_class_path = {cl : path +"/"+cl for cl in class_list}
    nb_img_per_class = {cl : len(os.listdir(dict_class_path[cl])) for cl in class_list}
    return nb_img_per_class


def pick_up_one_painting_per_class(path):
    """
    pick-up randomly one image per class and return a dictionnary.
    key: class(string) - value: image path
    The database must be divided into folders (one folder per class).
    arguments:
    * path: path of the dataset (by default: current path)
    """
    class_list = os.listdir(path)
    dict_class_path = {cl : path +"/"+cl for cl in class_list}
    dict_random_img_path = {cl: dict_class_path[cl]+"/"+random.choice(os.listdir(dict_class_path[cl])) for cl in class_list}
    one_painting_per_class = {cl : dict_random_img_path[cl] for cl in class_list}
    return one_painting_per_class


def random_painting(path):
    """
    return a tuple from a dataset of images: a random image(a path) and its class(string)
    The database must be divided into folders (one folder per class).
    arguments:
    * path: path of the dataset
    """
    one_painting_per_class = pick_up_one_painting_per_class(path)
    random_class = random.choice(list(one_painting_per_class.keys()))
    return one_painting_per_class[random_class], random_class


if __name__ == '__main__':

    #testing updated pick_up_one_painting_per_class
    path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    a = pick_up_one_painting_per_class(path)
    b = random_painting(path)
    c = number_img_per_class(path)
    print("pick_up_one_painting_per_class")
    print(a)
    print("random_painting")
    print(b)
    print("number_img_per_class")
    print(c)

    #testing pick_up_one_painting_per_class
    #path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    #imgs = pick_up_one_painting_per_class(path)
    #figure, axs = plt.subplots(1, 6, figsize=(20,20))
    #i = 0
    #for cl in imgs:
    #    axs[i].imshow(imgs[cl]/255)
    #    axs[i].set_title(cl)
    #    i += 1
    #plt.show()

    #testing number_img_per_class
    #path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    #print(number_img_per_class(path))

    #Uncomment for testing random_painting
    #path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    #img_height=180
    #img_width=180
    #painting, painting_class = random_painting(path)
    #plt.imshow(painting/255)
    #plt.title(painting_class)
    #plt.show()

    #Uncomment for testing display_paintings_and_classes
    #path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    #batch_size=1
    #validation_split=0.2
    #train_ds, test_ds = load_and_divide_dataset(
    #    path=path,
    #    img_height=img_height,
    #    img_width=img_width,
    #    batch_size=batch_size,
    #    validation_split=validation_split)
    #class_names_dict = classes_names_to_dict(train_ds)
    #display_paintings_and_classes(test_ds, n=10)
