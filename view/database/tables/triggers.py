import datetime
import telebot
from view.database.base import DB
import view.database.tables as tables
from view.database.tables.question_table import QuestionDB, SectionQuestionDB
from view.database.db_setting import *


class Triggers(DB):
    def __init__(self):
        super().__init__(db_name)

    def init_user_delete(self):
        request = f"""CREATE TRIGGER IF NOT EXISTS user_delete BEFORE DELETE
                                    ON { tables.user_table.UserDB.table_name }
                                    BEGIN
                                    DELETE FROM { tables.profile_table.ProfileDB.table_name } WHERE user_id = OLD.tg_id;
                                    END;
                                """
        self.cursor.execute(request)

    def init_section_question_delete(self):
        request = f"""CREATE TRIGGER IF NOT EXISTS section_question_question BEFORE DELETE
                                    ON { SectionQuestionDB.table_name }
                                    BEGIN
                                    DELETE FROM { QuestionDB.table_name } WHERE id = 
                                    OLD.section_id; END; """
        self.cursor.execute(request)