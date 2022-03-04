import telebot
from telebot import types
from datetime import datetime, timedelta


def time_module(bot):
    @bot.message_handler(commands=['time'])
    def show_time(m):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        itembtn1 = types.KeyboardButton('Now')
        itembtn2 = types.KeyboardButton('After 2 hours')
        markup.add(itembtn1, itembtn2)
        bot.send_message(m.chat.id, "What time would you want to know?", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def console_handler(m):
        text = m.text
        if text == 'Now':
            bot.send_message(m.chat.id, datetime.now().strftime("%H:%M:%S"))
        elif text == 'After 2 hours':
            bot.send_message(m.chat.id, (datetime.now() + timedelta(hours=2)).strftime("%H:%M:%S"))
