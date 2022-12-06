import telebot
import view.main_modules.random_phrases as dialog
from view.main_modules.menu import get_default_menu

from view.database.tables import user_table


def subscribe_user(message: telebot.types.Message, bot: telebot.TeleBot):
    user = message.from_user
    if user_table.is_exist(user.id):
        bot.send_message(user.id, dialog.subscribe_exist(), reply_markup=get_default_menu())
    else:
        try:
            user_table.add_user(user)
            bot.send_message(user.id, dialog.subscribe(), reply_markup=get_default_menu())
        except Exception:
            print("Ошибка при создании пользователя")
            bot.send_message(user.id, dialog.error(), reply_markup=get_default_menu())


# def unsubscribe_user(message: telebot.types.Message, bot: telebot.TeleBot):
#     user = message.from_user
#     if not user_table.is_exist(user.id):
#         bot.send_message(user.id, dialog.error(), reply_markup=get_default_menu())
#     else:
#         try:
#             user_table.delete_user(user.id)
#             bot.send_message(user.id, dialog.unsubscribe(), reply_markup=get_default_menu())
