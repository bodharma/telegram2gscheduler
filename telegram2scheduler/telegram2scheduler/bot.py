import telebot
import config
import datetime
import pytz
import json
import traceback
import re

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
   bot.send_message(
       message.chat.id,
       'Greetings! I can help you to add your events in the Google Calendar.\n' +
       'To activate the bot, follow the instructions.\n' +
       'To get instructions use /help.'
   )

@bot.message_handler(regexp="") # Need to add regular expression that will identify the date in the message
def function_name(message):
	bot.reply_to(message, "This is a message handler")

bot.polling(none_stop=True)

