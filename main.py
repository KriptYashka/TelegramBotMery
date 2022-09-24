import re
import uuid
import os
import telebot

from view import random_phrases as dialog
from view.menu import get_default_menu
from view.commands import mery_cmd
from view.database.db_initial import db_init
from brench_communicate.media import send_photo
from voice.test_laptop import VoiceRecognize

os.environ['MERY_TOKEN'] = '5052598391:AAEBBvip6Th7wgzYNxNHdDlErVdt64zStis'
token = os.environ['MERY_TOKEN']
bot = telebot.TeleBot(token, parse_mode=None)
db_init()


@bot.message_handler(commands=['start'])
def start_command(message: telebot.types.Message):
    text = "Приветствую тебя, <b>{}</b>!".format(message.from_user.username)
    bot.send_message(message.from_user.id, text, parse_mode="HTML")
    bot.send_video(message.from_user.id, open('KriptBot/media/photo/4.gif', 'rb'))
    text = "Чем сегодня займемся, мяу? ^_^"
    bot.send_message(message.from_user.id, text, parse_mode="HTML", reply_markup=get_default_menu())


@bot.message_handler(func=lambda message: True)
def listen_text_message(message: telebot.types.Message):
    msg_text = message.text.lower()

    #  Определение команд для пользователя
    actions = mery_cmd
    for regular, action in actions.items():
        if re.search(regular, msg_text):
            action(message, bot)
            return

    bot.send_message(message.from_user.id, dialog.unknown_command(), reply_markup=get_default_menu())


@bot.message_handler(content_types=["photo", "sticker", "audio"])
def listen_photo_message(message: telebot.types.Message):
    send_photo(message, bot)


@bot.message_handler(content_types=["voice"])
def listen_voice_message(message: telebot.types.Message):
    vr = VoiceRecognize()
    vr.recognize(bot, message)


def main():
    print("Бот запущен")
    bot.polling()


if __name__ == '__main__':
    main()
