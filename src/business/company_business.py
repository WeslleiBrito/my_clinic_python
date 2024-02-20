from src.database.companies_database import CompaniesDatabase
from src.services.validate_cnpj_cpf import ValidateCPFCNPJ
from src.dtos.company.input_edit_company import EditCompanySchema
from src.error.duplicity_error import DuplicityError
from src.error.not_found_error import NotFoundError
from marshmallow import ValidationError
import locale
import uuid

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


class CompaniesBusiness(CompaniesDatabase):

    def __init__(self):
        super().__init__()

    def findCompanyAll(self, order: bool = False):
        result = self._findCompanyAll_db()

        datas = []
        for row in result:
            data = {
                "id": row.id,
                "name": row.name,
                "cnpj": row.cnpj,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }

            datas.append(data)

        return sorted(datas, key=lambda x: locale.strxfrm(x['name']), reverse=order)

    def findCompanyById(self, id: str):
        result = self._findCompanyById_db(id=id)
        return result

    def findCompanyByName(self, name: str, order: bool = False):
        result = self._findCompanyByName_db(name)
        datas = []
        for row in result:
            data = {
                "id": row.id,
                "name": row.name,
                "cnpj": row.cnpj,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }

            datas.append(data)

        return sorted(datas, key=lambda x: locale.strxfrm(x['name']), reverse=order)

    def create_company(self, name: str, cnpj: str):

        message_error = {}

        if len(name) < 3:
            message_error["name"] = "O nome precisa ter pelo menos 3 caracteres."

        cnpj_exist = self._findCompanyByCNPJ_db(cnpj="".join(filter(str.isdigit, cnpj)))

        validate_cnpj = ValidateCPFCNPJ().validate(cnpj)

        if not validate_cnpj["status"]:
            message_error["cnpj"] = validate_cnpj["message"]

        if len(message_error) > 0:
            raise ValueError(message_error)

        if cnpj_exist:
            raise DuplicityError("O cnpj informado já existe em nossa base de dados.")

        name_exist = self._findCompanyByName_db(name=name.lower())

        if name_exist:
            raise DuplicityError("O nome informado já existe em nossa base de dados.")

        id = uuid.uuid4()

        self._create_company(
            id,
            name,
            "".join(filter(str.isdigit, cnpj))
        )

        print("Cadastro efetuado com sucesso!")

    def edit_company(self, id: str, name: str | None = None, cnpj: str | None = None):
        try:

            id_exist = self.findCompanyById(id)

            if not id_exist:
                raise NotFoundError("O id informado não existe")

            name = name or id_exist.name
            cnpj = cnpj or id_exist.cnpj

            EditCompanySchema().load({
                "name": name,
                "cnpj": cnpj
            })

            if (name):

                name_exist = self._findCompanyByName_db(name=name.lower())

                if name_exist and (name_exist.id != id_exist.id):
                    raise DuplicityError("O nome informado já exite em nossa base de dados.")

            if (cnpj):

                cnpj_exist = self._findCompanyByCNPJ_db(cnpj="".join(filter(str.isdigit, cnpj)))

                if cnpj_exist and (cnpj_exist.id != id_exist.id):
                    raise DuplicityError("O cnpj informado já exite em nossa base de dados.")

            self._edit_company(
                id,
                name,
                "".join(filter(str.isdigit, cnpj))
            )

            print("Edição efeuado com sucesso!")
        except ValidationError as error:
            print(error.messages)

    def delete_company(self, id: str):
        try:
            company_exist = self.findCompanyById(id)

            if not company_exist:
                raise NotFoundError("O id informado não existe")

            self._delete_company(id)
            print("Registro deletado com sucesso!")
        except ValidationError as error:
            print(error.messages)


if __name__ == "__main__":
    class_business = CompaniesBusiness()
    class_business.create_company("Sabrina e Thiago Limpeza ME", "26.060.317/0001-07")
    result = class_business.findCompanyAll()

    for r in result:
        print(r)
