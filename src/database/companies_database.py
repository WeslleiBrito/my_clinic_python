from src.connection.connection_db import ConnectionDB
from src.entities.companies import Companies
from sqlalchemy.exc import IntegrityError
from src.error.operation_not_completed_error import OperationNotCompletedError
from sqlalchemy import func
from datetime import datetime

class CompaniesDatabase:

    def _findCompanyAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).all()
            return result

    def _findCompanyById_db(self, id: str):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).filter_by(id=id).first()
            return result

    def _findCompanyByCNPJ_db(self, cnpj: str):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).filter_by(cnpj=cnpj).first()
            return result

    def _findCompanyByName_db(self, name: str):

        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).filter(func.lower(Companies.name) == func.lower(name)).first()
            return result

    def _create_company(self, id: str, name: str, cnpj: str):
        with ConnectionDB() as db:
            newDatas = Companies(id, name, cnpj)

            try:
                db.create_table_if_not_exists("companies", Companies)
                db.session.add(newDatas)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                raise OperationNotCompletedError("Tivemos um problema ao inserir os novos dados: ") from e

    def _edit_company(self, id: str, name: str, cnpj: str):

        try:
            with ConnectionDB() as db:
                db.create_table_if_not_exists("companies", Companies)
                company_db = db.session.query(Companies).filter_by(id=id).first()
                company_db.name = name
                company_db.cnpj = cnpj
                company_db.updated_at = datetime.now()
                db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise OperationNotCompletedError("Tivemos um problema ao editar os dados: ") from e
