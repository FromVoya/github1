import get_currency_price


def currency_value(meaning: str) -> str:
    """
    Function for change variable from float to str
    :param meaning:str-variable currency
    :return:str-currency in string
    """
    currency = float(get_currency_price.get_currency_price(meaning))
    return str(currency)
