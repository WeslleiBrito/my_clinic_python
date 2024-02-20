from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

data_connection = {
    "user": os.environ["user"],
    "password": os.environ["password"],
    "path": os.environ["pathdatabase"],
    "port": os.environ["port"],
    "namedatabase": os.environ["namedatabase"]
}


class ConnectionDB:

    def __init__(self) -> None:
        self.__path_database = f"mysql+pymysql://{data_connection['user']}:{data_connection['password']}@{data_connection['path']}:{data_connection['port']}/{data_connection['namedatabase']}"
        self.__engine = self.__create_database_engine()
        self.__metadata = MetaData()
        self.__metadata.bind = self.__engine
        self.session = None

    def __create_database_engine(self):
        try:
            engine = create_engine(self.__path_database)
            return engine
        except Exception as e:
            raise ("Erro ao conectar com o banco de dados.", e)

    def get_engine(self):
        return self.__engine

    def table_exists(self, table_name):
        return self.__metadata.tables.get(table_name) is not None

    def create_table_if_not_exists(self, table_name, table_definition):
        if not self.table_exists(table_name):
            table_definition.metadata.create_all(self.__engine)

    def __enter__(self):
        try:
            session_make = sessionmaker(bind=self.__engine)
            self.session = session_make()
            return self
        except Exception as e:
            raise ("Conectamos ao banco, porem não foi possível criar a sessão.", e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
