from telebot import types


def set_commands(bot):
    bot.set_my_commands([
        types.BotCommand('time', 'Показывает текущее время')
    ])