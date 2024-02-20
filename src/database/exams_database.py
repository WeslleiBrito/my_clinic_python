from src.connection.connection_db import ConnectionDB
from src.entities.exams import Exams


class ExamsDatabase:

    def findExamsAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Exams)
            result = db.session.query(Exams).all()
            return result