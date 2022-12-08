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
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title TEXT,
                datetime_finish DATETIME
                );""".format(self.table_name)
        self.cursor.execute(request)

    def is_exist(self, profile_id: int):
        obj = self.select(self.table_name, "id", profile_id)
        return len(obj)

    def append(self, title, datetime_finish=None):
        date = [title]
        col_fields = ["title"]
        if datetime_finish:
            date.append(datetime_finish)
            col_fields.append("datetime_finish")
        self.insert(self.table_name, date, col_fields)


class QuestionDB(DB):
    table_name = "question"

    def __init__(self):
        super().__init__(db_name)

    def init_table(self):
        """
        Создает таблицу вопросов
        """
        request = """CREATE TABLE IF NOT EXISTS {} (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
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
