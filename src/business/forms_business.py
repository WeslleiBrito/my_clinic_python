from src.database.forms_database import FormsDatabase


class FormsBusiness(FormsDatabase):

    def __init__(self):
        super().__init__()

    def findFormsAll(self):
        result = self.findFormsAll_db()

        datas = []
        for row in result:
            data = {
                "id": row.id,
                "idTypeExam": row.id_type_exam,
                "idCompany": row.id_company,
                "nameCompany": row.name_company,
                "idPatient": row.id_patient,
                "namePatient": row.name_patient,
                "rg": row.rg,
                "cnpj": row.cnpj,
                "cpf": row.cpf,
                "functionPatient": row.function_patient,
                "numberProcedures": row.number_procedures,
                "statusExam": row.status_exam,
                "amount": row.amount,
                "comments": row.comments,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }

            datas.append(data)

        return datas


if __name__ == "__main__":
    class_form = FormsBusiness()
    datas = class_form.findFormsAll()
    print(datas)
