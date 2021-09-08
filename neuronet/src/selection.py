import numpy as np
import random


def probability(x_test, model):
    # creating a random number
    n = round(random.random() * 100) * round(random.random() * 10)

    # adding an axis(so that it is two-dimensional)
    x = np.expand_dims(x_test[n], axis=0)

    # output result of neural network processing
    res = model.predict(x)

    # creating an empty list
    values_str = []

    # creating a list and adding the probability for each digit to it as a string variable
    for i in res:
        for j in range(10):
            if (str(i[j])[2:4]) == "00":
                values_str.append('0')
                continue
            elif (str(i[j])[2:3]) == "0":
                values_str.append((str(i[j]))[3:4])
                continue
            else:
                values_str.append(((str(i[j]))[2:4]))

    values_int = []

    # overriding a list with probabilities to a list of int variables
    for i in values_str:
        i = int(i)
        values_int.append(i)

    return values_int, n
