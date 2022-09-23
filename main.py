import telebot
import re
import uuid
from view.menu import get_default_menu
from view.commands import mery_cmd
from view import random_phrases as dialog
from voice.test import VoiceRecognition
import os

from brench_communicate.media import send_photo

token = "5052598391:AAEBBvip6Th7wgzYNxNHdDlErVdt64zStis"  # Не смейте трогать моего бота! Меняйте токен
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start_command(message):
    text = "Приветствую тебя, <b>{}</b>!".format(message.from_user.username)
    bot.send_message(message.from_user.id, text, parse_mode="HTML")
    bot.send_video(message.from_user.id, open('KriptBot/media/photo/4.gif', 'rb'))
    text = "Чем сегодня займемся, мяу? ^_^"
    bot.send_message(message.from_user.id, text, parse_mode="HTML", reply_markup=get_default_menu())


@bot.message_handler(func=lambda message: True)
def listen_text_message(message):
    msg_text = message.text.lower()

    #  Определение команд для пользователя
    actions = mery_cmd
    for regular, action in actions.items():
        if re.search(regular, msg_text):
            action(message, bot)
            return

    bot.send_message(message.from_user.id, dialog.dont_know(), reply_markup=get_default_menu())


@bot.message_handler(content_types=["photo", "sticker", "audio"])
def listen_photo_message(message: telebot.types.Message):
    send_photo(message, bot)


@bot.message_handler(content_types=["voice"])
def listen_voice_message(message: telebot.types.Message):
    filename = str(uuid.uuid4())
    file_name_full = "./voice/" + filename + ".ogg"
    file_name_full_converted = "./voice/" + filename + "_conv.wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)
    os.system("ffmpeg -i " + file_name_full + "  " + file_name_full_converted)


def main():
    print("Бот запущен")
    bot.polling()


if __name__ == '__main__':
    main()
