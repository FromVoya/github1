from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
import os.path
import config.config as conf

# Protecting from error:
# This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU
# instructions in performance-critical operations
# DISABLING THE DEBUG LOG (WARNING + ERROR + FATAL)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def neuronet(x_train: int, y_train_cat: int) -> None:
    """
    Creating neuronet
    Saving trained neuronet to file

    :param x_train: int- standardization of input data
    :param y_train_cat: int -converting digits as a vector
    """
    model = keras.Sequential([
        Flatten(input_shape=(28, 28, 1)),
        # special type of layer (Flatten) - transformation of 28x28 matrix into layer from vector of 784 elements long.
        #  1 means 1 pixel
        Dense(128, activation='relu'),  # connects the neurons of the input layer with the hidden one
        Dense(10, activation='softmax')  # connects the neurons of the hidden layer to the output layer
    ])

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Starting the training process: 80% - training sample, 20% - validation sample
    model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)
    # model.fit - launching the training model
    # x_train - input training set
    # y_train_cat - required values at the output of the neural network(in the form of a vector)
    # batch_size=32 - the size of the butch (after every 32 images, the weight coefficients are adjusted)
    # epochs=5 - number of epochs
    # validation_split=0.2 - splitting the training sample

    model.save(conf.path)
