import requests
from bs4 import BeautifulSoup
import config.config as conf
import base64


def get_currency_price(site_of_currency: str) -> float:
    """

    :param site_of_currency:str-named of site
    :return: float-value of currency
    """

    header_cod = base64.b64decode(conf.headers)
    header_decod = header_cod.decode('utf-8')

    # the user who passes by URL address(without this line it will don't work
    headers = {
        'User-Agent': header_decod}
    # request by url
    full_page = requests.get(site_of_currency, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", conf.convert)
    return convert[0].text
