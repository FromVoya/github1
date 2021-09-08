import scr.currency
import scr.solution
import config.config as conf
import config.config_history as confhist
import telebot
import choose_currency
import message_options
import base64
import variation_of_answers

token = base64.b64decode(conf.token)
bot = telebot.TeleBot(token.decode('utf-8'))


# start bot
@bot.message_handler(content_types=['text'])
# Ask user what does he want
def start(message) -> None:
    """
    Start working bot.
    :param message: str-message creating user
    """
    message.text = message_options.lower_registr(message.text)
    meaning = variation_of_answers.cross(message.text)
    if meaning == conf.course:
        bot.send_message(message.from_user.id, conf.text_currency)
        bot.register_next_step_handler(message, answer_currency)
    elif meaning == conf.history:
        bot.send_message(message.from_user.id, conf.text_history)
        bot.register_next_step_handler(message, answ_history)


    else:
        bot.send_message(message.from_user.id, conf.text_dont_under1)


def answer_currency(message) -> None:
    """
    Answer user on question with currency course
    :param message: str-answer user on question with currency course
    """
    message.text = choose_currency.choose(message.text)

    if message.text == conf.usd_text:
        bot.send_message(message.from_user.id, conf.message % (conf.usd, scr.currency.currency(message.text)))
    elif message.text == conf.eur_text:
        bot.send_message(message.from_user.id, conf.message % (conf.eur, scr.currency.currency(message.text)))
    elif message.text == conf.gbp:
        bot.send_message(message.from_user.id, conf.message % (conf.gbp, scr.currency.currency(message.text)))
    elif message.text == conf.cny_text:
        bot.send_message(message.from_user.id, conf.message % (conf.cny, scr.currency.currency(message.text)))
    elif message.text == conf.chf_text:
        bot.send_message(message.from_user.id, conf.message % (conf.chf, scr.currency.currency(message.text)))
    else:
        bot.send_message(message.from_user.id, conf.text_dont_under2)
        bot.register_next_step_handler(message, answer_currency)


def answ_history(message) -> None:
    """
    Answer user on question with currency history
    :param message: str-answer user on question with currency history
    """
    message.text = choose_currency.choose(message.text)
    if message.text == conf.usd_text:
        bot.send_message(message.from_user.id, confhist.usd)

    elif message.text == conf.eur_text:
        bot.send_message(message.from_user.id, confhist.eur)
    elif message.text == conf.gbp_text:
        bot.send_message(message.from_user.id, confhist.gbp)
    elif message.text == conf.cny_text:
        bot.send_message(message.from_user.id, confhist.cny)
    elif message.text == conf.chf_text:
        bot.send_message(message.from_user.id, confhist.chf)
    else:
        bot.send_message(message.from_user.id, conf.text_dont_under2)
        bot.register_next_step_handler(message, answ_history)


bot.polling(none_stop=True, interval=0)
