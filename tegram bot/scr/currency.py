import currency_value
import config.config as conf


def currency(name_valute: str) -> float:
    """
    Function for defined site with certain currency by it's key
    :param name_valute:str-name of currency(valute)
    :return:float-value of currency
    """
    # Variable for create site with currency
    site_of_currency = conf.site_of_currency % name_valute

    return float(currency_value.currency_value(site_of_currency))


