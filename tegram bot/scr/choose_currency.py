import config.config


def choose(message: str) -> str:
    """
    Function for choose defined currency by any variation this currency
    :param message: str-variation of writing currency
    :return:str-key this currency
    """
    currency_dict = config.config.currency_dict

    def country(currency):
        for i, j in currency.items():
            if message in j:
                return i

    return country(currency_dict)
