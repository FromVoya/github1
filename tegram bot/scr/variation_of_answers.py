import config.config as conf


def cross(first: str) -> str:
    """
    The function define meaning message which user is write
    :param first: str- message written by the user
    :return: str- the key word which direct next message
    """
    input_data = [first]
    variation_of_variables = [conf.course, conf.history_short]

    for j in variation_of_variables:
        a = [i for i in range(len(input_data)) if j in input_data[i]]

        if a == [0]:
            if j == variation_of_variables[0]:
                return conf.course
            elif j == variation_of_variables[1]:
                return conf.history
