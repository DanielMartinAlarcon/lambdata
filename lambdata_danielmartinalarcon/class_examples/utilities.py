from sklearn.model_selection import train_test_split


class Complex:
    def __init__(self, realpart, imagpart):
        """
        Instantiates the complex number with a real and an imaginary part
        """
        num_type = (int, float)

        if isinstance(realpart, num_type) and isinstance(imagpart, num_type):
            self.r = realpart
            self.i = imagpart
        else:
            print("Hey, that's not a number!")

    def add(self, real, imag):
        """
        Takes a new complex number and adds it to the one that the class was
        originally instantiated with.
        """
        new_real = self.r + real
        new_imag = self.i + imag

        return Complex(new_real, new_imag)


def train_validation_test_split(
        X, y, train_size=0.8, val_size=0.1, test_size=0.1,
        random_state=None, shuffle=True):
    """
    Custom function for making train-validate-test splits.

    Inputs
    -------
    X : Acceptable inputs for sklearn.model_selection.train_test_split,
        which include lists, numpy arrays, scipy-sparse matrices or
        pandas dataframes
    Features of the dataset

    y : Same type as X
    Observations in the dataset

    train_size, val_size, test_size : float
    Proportions of the datapoints to go into the training, validation,
    and test sets, respectively.

    Outputs
    -----------
    X_train, X_val, X_test, y_train, y_val, y_test : Same type as X,y
        Divided datasets
    """
    assert train_size + val_size + test_size == 1

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size/(train_size+val_size),
        random_state=random_state, shuffle=shuffle)

    return X_train, X_val, X_test, y_train, y_val, y_test

import seaborn as sns 

def confusion_matrix_viz(y_true, y_pred):
    """
    confusion matrix in a visualization format
    """ 
    matrix = confusion_matrix(y_true, y_pred)
return sns.heatmap(matrix, annot=True, fmt=",", linewidths=1,
                   linecolor='grey', sqaure=True, 
                   xticklabels=['Predicted\nNo', 'Predicted\nYes'],
                   yticklabels=['Actaul\nNo', 'Actaul\nYes'])
