import datetime
import telebot
from view.database.base import DB
from view.database.tables.user_table import UserDB
from view.database.db_setting import *


class ProfileDB(DB):
    table_name = "profile"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу профилей пользователей
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INT PRIMARY KEY,
                user_id INT,
                name TEXT,
                birthday DATE,
                datetime_join DATETIME,
                status TEXT
                );""".format(self.table_name)
        self.cursor.execute(request)


    def is_exist(self, user_id: int):
        obj = self.select(self.table_name, "id", user_id)
        return len(obj)

    def add_user(self, user: telebot.types.User, status="common"):
        data = [
            user.id, datetime.datetime.now().isoformat(), status
        ]
        self.insert(self.table_name, data)

    def delete_user(self, user_id: int):
        self.delete(self.table_name, "id", user_id)
        request = """CREATE TRIGGER my_u_log BEFORE INSERT
                    ON users
                    BEGIN
                    INSERT INTO user_log(id_u, u_date) VALUES (NEW.id, datetime('now'));
                    END;
                """
