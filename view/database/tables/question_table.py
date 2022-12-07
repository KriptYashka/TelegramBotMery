import datetime
import telebot
from view.database.base import DB
from view.database.db_setting import *


class SectionQuestionDB(DB):
    table_name = "section_question"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу секций вопросов
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INT PRIMARY KEY,
                title TEXT,
                datetime_finish DATETIME
                );""".format(self.table_name)
        self.cursor.execute(request)

    def is_exist(self, profile_id: int):
        obj = self.select(self.table_name, "id", profile_id)
        return len(obj)


class QuestionDB(DB):
    table_name = "question"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу вопросов
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INT PRIMARY KEY,
                section_id INT,
                title TEXT,
                answer TEXT,
                short_answer TEXT,
                url TEXT,
                image_url TEXT
                );""".format(self.table_name)
        self.cursor.execute(request)

    def is_exist(self, profile_id: int):
        obj = self.select(self.table_name, "id", profile_id)
        return len(obj)
