from view.database.base import DB
from view.database.tables.user_table import UserDB
from view.database.tables.profile_table import ProfileDB
from view.database.tables.stream_table import StreamDB
from view.database.tables.triggers import Triggers
from view.database.tables.question_table import QuestionDB, SectionQuestionDB
from view.database.db_setting import *


def db_init():
    """
    Инициализация всех таблиц и триггеров БД
    """
    # Таблицы
    tables = [UserDB(), ProfileDB(), StreamDB(), QuestionDB(), SectionQuestionDB()]
    for table in tables:
        table.init_table()

    # Триггеры
    Triggers().init_user_delete()
    Triggers().init_section_question_delete()