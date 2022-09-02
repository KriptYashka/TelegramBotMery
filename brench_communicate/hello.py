import random

import telebot
import view.random_phrases as dialog
from view.menu import get_default_menu, button_menu


def send_hello(message, bot):
    user_id = message.from_user.id
    bot.send_message(user_id, dialog.hello(message.from_user.username), reply_markup=get_default_menu())


def send_how_are_you(message, bot):
    user_id = message.from_user.id
    bot.send_message(user_id, dialog.how_are_you(), reply_markup=get_default_menu())


def send_joke(message, bot):
    user_id = message.from_user.id
    want_fish = random.randint(0, 10)
    if want_fish <= 2:
        fish = random.choice("🐡🐠🐟")
        bot.send_message(user_id, dialog.joke_for_fish(fish), reply_markup=button_menu(["🐡", "🐠", "🐟"]))
        bot.register_next_step_handler(message, joke_for_fish, bot, fish)
        return
    bot.send_message(user_id, dialog.joke(), reply_markup=get_default_menu())


def joke_for_fish(message, bot, fish):
    user_id = message.from_user.id
    if message.text.count(fish):
        bot.send_message(user_id, dialog.joke(), reply_markup=get_default_menu())
    else:
        bot.send_message(user_id, "Ну и ладно...", reply_markup=get_default_menu())


