import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras.models import load_model
import os.path
import src.neuro_network as neuro
import src.selection as selection
import config.config as conf

# загрузка изображений из mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# стандартизация входных данных
x_train = x_train / 255
x_test = x_test / 255

# преобразование цифр в виде вектора
y_train_cat = keras.utils.to_categorical(y_train, 10)

# checking the existence of a trained neuronet
if not os.path.exists(conf.path):
    neuro.neuronet(x_train, y_train_cat)

# loading a trained neuronet
model = load_model(conf.path)

# call the function which return by index:
# [0] - the list with probabilities of numbers
# [1] - random number for creating random picture
value = selection.probability(x_test, model)

# create diagram with random picture from mnist
plt.imshow(x_test[value[1]], cmap=plt.cm.binary)
plt.show()

# diagram with probabilities of  every numbers from 0 to 9
plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], value[0])
plt.show()
