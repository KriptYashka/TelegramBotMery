import telebot
import view.random_phrases as dialog
from view.menu import get_default_menu


def send_weather_yesterday(message, bot):
    user_id = message.from_user.id
    bot.send_message(user_id, dialog.yesterday_weather(), reply_markup=get_default_menu())

