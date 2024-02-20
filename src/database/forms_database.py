from src.connection.connection_db import ConnectionDB
from src.entities.forms import Forms


class FormsDatabase:

    def findFormsAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Forms)
            result = db.session.query(Forms).all()
            return result