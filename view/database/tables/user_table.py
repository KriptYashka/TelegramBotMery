import datetime
import telebot
from view.database.base import DB
from view.database.db_setting import *

table_name = "users"


def init_table():
    """
    Создает таблицу пользователей
    """
    request = """CREATE TABLE IF NOT EXISTS {} (
            id INT PRIMARY KEY,
            datetime_join DATETIME,
            status TEXT
            );""".format(table_name)
    DB(db_name).cursor.execute(request)


def is_exist(user_id: int):
    db = DB(db_name)
    obj = db.select(table_name, "id", user_id)
    return len(obj)


def add_user(user: telebot.types.User, status="common"):
    db = DB(db_name)
    data = [
        user.id, datetime.datetime.now().isoformat(), status
    ]
    db.insert(table_name, data)


def delete_user(user_id: int):
    db = DB(db_name)
    db.delete(table_name, "id", user_id)
