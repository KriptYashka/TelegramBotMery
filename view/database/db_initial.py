from view.database.base import DB
from view.database.tables import user_table
from view.database.db_setting import *


def db_init():
    """
    Инициализация всех таблиц БД
    """
    user_table.init_table()