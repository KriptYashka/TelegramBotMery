import datetime
import telebot
from view.database.base import DB
from view.database.tables.user_table import UserDB
from view.database.db_setting import *


class StreamDB(DB):
    table_name = "streams"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу профилей пользователей
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title TEXT,
                description TEXT
                );""".format(self.table_name)
        self.cursor.execute(request)
