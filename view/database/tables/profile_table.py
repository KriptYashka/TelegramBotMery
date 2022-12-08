import datetime
import telebot
from view.database.base import DB
from view.database.db_setting import *


class ProfileDB(DB):
    table_name = "profiles"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу профилей пользователей
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_id INT,
                datetime_join DATETIME,
                status TEXT,
                name TEXT,
                birthday DATE
                );""".format(self.table_name)
        self.cursor.execute(request)

    def is_exist(self, profile_id: int):
        obj = self.select(self.table_name, "id", profile_id)
        return len(obj)

    def add_profile(self, user: telebot.types.User, status="common"):
        data = [
            user.id, datetime.datetime.now().isoformat(), status
        ]
        self.insert(self.table_name, data)

    def delete_profile(self, profile_id: int):
        self.delete(self.table_name, "id", profile_id)
