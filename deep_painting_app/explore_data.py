import math
import matplotlib.pyplot as plt
from deep_painting_app.data_processing import load_and_divide_dataset, classes_names_to_dict, give_class_name


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
    display_paintings_and_classes(test_ds, n=10)
