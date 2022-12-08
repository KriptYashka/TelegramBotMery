import datetime
import telebot
from view.database.base import DB
from view.database.tables.profile_table import ProfileDB
from view.database.db_setting import *


class UserDB(DB):
    table_name = "users"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу пользователей
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                profile_id INT
                );""".format(self.table_name)
        self.cursor.execute(request)

    def is_exist(self, user_id: int):
        obj = self.select(self.table_name, "id", user_id)
        return len(obj)

    def append(self, user: telebot.types.User):
        # profile_db = ProfileDB()
        # profile_db.add_profile(user)
        data = [
            user.id, "1"
        ]
        self.insert(self.table_name, data)

    def delete_by_id(self, user_id: int):
        self.delete(self.table_name, "id", user_id)
