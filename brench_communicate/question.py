import datetime
import os
import random
import telebot
from telebot import types  # для указание типов

from view.database.tables import question_table

import view.main_modules.random_phrases as dialog
from view.main_modules.menu import get_default_menu, button_menu


def branch_add_section(message: telebot.types.Message, bot):
    @bot.callback_query_handler(func=lambda call: True)
    def handle_query(call):
        if call.data == "как вводить дату":
            bot.answer_callback_query(call.id, show_alert=True, text="Пример:\n16.03.2022")

    def ask_add_section(message: telebot.types.Message, bot):
        user_id = message.from_user.id
        text = dialog.add_section(1)
        bot.send_message(user_id, text, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ask_date_add_section, bot)

    def ask_date_add_section(message: telebot.types.Message, bot):
        user_id = message.from_user.id
        text = dialog.add_section(2)
        theme = message.text

        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("Как вводить дату?", callback_data="как вводить дату")
        markup.add(button)

        bot.send_message(user_id, text, reply_markup=markup, parse_mode="Markdown")
        bot.send_message(user_id, "Этот шаг можно пропустить", reply_markup=button_menu(["Пропустить"]))
        bot.register_next_step_handler(message, confirm_add_section, bot, theme)

    def correct_datetime(datetime_final):
        items = datetime_final.split(".")
        if len(items) == 3:
            try:
                datetime.datetime(int(items[0]), int(items[1]), int(items[2]))
                return True
            except ValueError:
                return False
        return False

    def confirm_add_section(message: telebot.types.Message, bot, theme):
        user_id = message.from_user.id
        datetime_finish = message.text
        if message.text.lower() == "пропустить" or not correct_datetime(datetime_finish):
            datetime_finish = None

        text = f"Правильно я тебя понимаю, новая тема для вопросов:\n\n**{theme}**"
        if datetime_finish:
            text += f"\nСрок: {datetime_finish}"

        bot.send_message(user_id, text, reply_markup=button_menu(["Да", "Нет"]), parse_mode="Markdown")
        bot.register_next_step_handler(message, do_add_section, bot, theme, datetime_finish)

    def do_add_section(message: telebot.types.Message, bot, theme, datetime_finish=None):
        if message.text.lower() == "да":
            if datetime_finish:
                day, month, year = map(int, datetime_finish.split("."))
                datetime_finish = datetime.datetime(year, month, day).isoformat()
            question_table.SectionQuestionDB().append(theme, datetime_finish)

            user_id = message.from_user.id
            text = dialog.add_section(0, theme, datetime_finish)
            bot.send_message(user_id, text, reply_markup=get_default_menu(), parse_mode="Markdown")

        else:
            bot.send_message(message.from_user.id, dialog.perplexity())

    # Основной код ветки

    ask_add_section(message, bot)


def branch_add_question(message: telebot.types.Message, bot: telebot.TeleBot):
    def ask_add_question(message: telebot.types.Message, bot: telebot.TeleBot):
        user_id = message.from_user.id
        text = dialog.add_question(1)
        bot.send_message(user_id, text, parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, ask_date_add_section, bot)