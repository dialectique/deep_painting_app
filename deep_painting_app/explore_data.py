

#Deep painting app
#Explore processing

#display_paintings_and_classes(dataset, n=1)
#random_painting(path, img_height=180, img_width=180)
#number_img_per_class
#pick_up_one_painting_per_class


import math
import random
import matplotlib.pyplot as plt
from deep_painting_app.data_processing import load_and_divide_dataset, classes_names_to_dict, give_class_name
from tensorflow.keras.preprocessing import image_dataset_from_directory


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


def random_painting(path, img_height=180, img_width=180):
    """
    return a tuple from a dataset of images: a random image(numpy ndarray) and its class(string)
    The database must be divided into folders (one folder per class).
    arguments:
    * path: path of the dataset (by default: current path)
    * image size: img_height and img_width. By default 180 for both
    """

    # raise an error if path is not a string
    if not type(path) is str:
        raise TypeError("path must be a string")

    # random seed value for image_dataset_from_directory
    random.seed()
    seed = random.randint(0,100)

    # load dataset from path
    dataset = image_dataset_from_directory(
        path,
        labels='inferred',
        label_mode='categorical',
        shuffle = True,
        seed = seed,
        image_size = (img_height, img_width),
        color_mode='rgb',
        batch_size=1)

    #iterates through dataset, set one painting and its class, randomly stop
    class_names_dict = classes_names_to_dict(dataset)
    for x, y in dataset.as_numpy_iterator():
        painting, painting_class = x[0], give_class_name(y[0], class_names_dict)
        if random.randint(0,1000) > 700:
            break

    return painting, painting_class

def number_img_per_class(path):
    """
    return a dictionnary (keys: class - values: number of images)
    argument: path of the dataset (by default: current path)
    The database must be divided into folders (one folder per class)
    """

    # load full dataset from path
    dataset = image_dataset_from_directory(
        path,
        labels='inferred',
        label_mode='categorical',
        batch_size=1)

    # set a dictionnary with the classes of the dataset
    nb_img_per_class = {c: 0 for c in dataset.class_names}

    # iterating the dataset and count images for each class
    class_names_dict = classes_names_to_dict(dataset)
    for x, y in dataset.as_numpy_iterator():
        nb_img_per_class[give_class_name(y[0], class_names_dict)] += 1

    return nb_img_per_class


def pick_up_one_painting_per_class(path, img_height=180, img_width=180):
    """
    pick-up randomly one image per class and return a dictionnary.
    key: class(string) - value: image(numpy ndarray)
    The database must be divided into folders (one folder per class).
    arguments:
    * path: path of the dataset (by default: current path)
    * image size: img_height and img_width. By default 180 for both
    """
    # random seed value for image_dataset_from_directory
    random.seed()
    seed = random.randint(0,100)

    # load full dataset from path
    dataset = image_dataset_from_directory(
        path,
        labels='inferred',
        label_mode='categorical',
        batch_size=1,
        seed = seed,
        image_size = (img_height, img_width))

    # dict of class names and corresponding vectors
    class_names_dict = classes_names_to_dict(dataset)

    # intitate a dictionnary: key = artistic mvt, value = list of paintings
    paintings_per_class = {c: [] for c in dataset.class_names}

    # iterate the dataset and choose the first encountered painting, for each class
    # the dataset has been load randomly already
    for cl in dataset.class_names:
        for painting, cla in dataset.as_numpy_iterator():
            if cl == give_class_name(cla[0], class_names_dict):
                paintings_per_class[give_class_name(cla[0], class_names_dict)] = painting[0]
                break
    return paintings_per_class


if __name__ == '__main__':

    #testing pick_up_one_painting_per_class
    path = "../raw_data/Portrait_Painting_Dataset_For_Different_Movements/orgImg"
    imgs = pick_up_one_painting_per_class(path)
    figure, axs = plt.subplots(1, 6, figsize=(20,20))
    i = 0
    for cl in imgs:
        axs[i].imshow(imgs[cl]/255)
        axs[i].set_title(cl)
        i += 1
    plt.show()

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
