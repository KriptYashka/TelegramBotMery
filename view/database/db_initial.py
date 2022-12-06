from view.database.base import DB
from view.database.tables import user_table, profile_table, triggers
from view.database.db_setting import *


def db_init():
    """
    Инициализация всех таблиц и триггеров БД
    """
    # Таблицы
    user_table.UserDB().init_table()
    profile_table.ProfileDB().init_table()

    # Триггеры
    triggers.Triggers().init_user_delete()