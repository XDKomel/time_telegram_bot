import telebot
from modules.time_module import time_module
from modules.commands import set_commands

token = '5189850186:AAHPqb5LybLL9uRTHkZKOHsIqn4HPD2OHGk'
bot = telebot.TeleBot(token)
set_commands(bot)  # устанавливаем подсказки
time_module(bot)  # устанавливаем модуль бота, который отвечает за время

bot.infinity_polling()





