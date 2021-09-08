"""_____________________________________________________________________
    Configuration file for the "Telegram bot" module
    Last modification: 09.08.2021
    Author of the modification: Chirgin Konstantin
    Email: ###
   _____________________________________________________________________"""
__version__ = '0.0.0'

"""_____________________________________________________________________
    Token for telegram's bot
        1. Name of token
   _____________________________________________________________________"""
"""1"""

# Decoding token by Base64
token = 'MTkzOTI1NTQ1MjpBQUZNM0twdmxoQUVfYUV4dmJCZm5sZG93bG94NkxyVjVjRQ=='

"""_____________________________________________________________________
    Variations of variable names
        1. Title
        2. Title history 
        3. Title history for choosing answer
        4. usd
        5. eur
        6. gbp
        7. cny 
        8. chf
   _____________________________________________________________________"""
"""8"""
course = 'курс'
history = 'история'
history_short = 'истори'
usd_text = 'usd'
eur_text = 'eur'
gbp_text = "gbp"
cny_text = 'cny'
chf_text = 'chf'

"""_____________________________________________________________________
    Text Template
        1. Currency
        2. History
        3. Don't understand
        4. Don't understand
   _____________________________________________________________________"""

text_currency = ("Напиши название интересующей тебя валюты:\n"
                 "💵 usd-доллар\n"
                 "💶 eur-евро\n"
                 "💷 gbp-фунт\n"
                 "💴 cny-юань\n"
                 "🇨🇭 chf-франк")

text_history = ("История какой валюты тебя интересует:\n"
                "💵доллар\n"
                "💶евро\n"
                "💷фунт\n"
                "💴юань или\n"
                "🇨🇭 франк?")

text_dont_under1 = 'Я тебя не понимаю. \nНапиши:  Курс валют или История валют'
text_dont_under2 = 'Я тебя не понимаю. \nКакя валюта тебя интересует?'

"""_____________________________________________________________________
    Currency
        1. usd
        2. eur
        3. gbp
        4. cny 
        5. chf
   _____________________________________________________________________"""

usd = f"💵\nКурс доллара:"
eur = f"💶\nКурс евро:"
gbp = f"💷\nКурс фунта:"
cny = f"💴\nКурс юаня:"
chf = f"🇨🇭\nКурс франка:"

"""_____________________________________________________________________
    Message for answer user on question with currency course
        First %s conf.currency
        Second %s scr.currency.currency("name of currency")
        
   _____________________________________________________________________"""
message = "%s %s рубля"


# Currency dictionary
currency_dict = {'usd': ['доллар', 'Доллар', 'Долар', 'долар', 'usd'],
                 'eur': ['Евро', 'евро', 'eur', 'euro'],
                 'gbp': ['Фунт', 'фунт', 'gbp'],
                 'cny': ['Юань', 'юань', 'cny', 'yuan'],
                 'chf': ['Франк', 'франк', 'chf', 'franc']}

# link with site of currency
site_of_currency = f"https://bankiros.ru/convert/%s-rub/1"

# headers decoded by Base64
headers=("TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykg"
         "Q2hyb21lLzkxLjAuNDQ3IDIuMTE0IFNhZmFyaS81MzcuMzYgRWRnLzkxLjAuODY0LjU0")

# convert for currency
convert = {"class": "xxx-fast-converter__out"}
