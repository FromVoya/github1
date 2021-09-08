# -*- coding: utf8 -*-
import scr.currency
import scr.solution
import config.config
import telebot
import start_bot
import choose_currency
import message_options
import base64

"""
Need:
    1. Create telegram bot which will send message with currency course and currency history
"""

# Create the Updater and pass the token.
bot = telebot.TeleBot(config.config.token)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
