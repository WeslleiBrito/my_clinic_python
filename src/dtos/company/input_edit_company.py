from marshmallow import Schema, fields, ValidationError, validate
from src.services.validate_cnpj_cpf import ValidateCPFCNPJ
from src.services.validate_UUID import validate_uuid
from pprint import pprint


class EditCompanySchema(Schema):
    name = fields.String(
        required=False,
        error_messages={"invalid": "Espera-se uma string."},
        validate=validate.Length(
            min=3,
            error="O nome precisa ter pelo menos 3 caracteres."
        )
    )
    cnpj = fields.String(
        required=False,
        error_messages={"invalid": "Espera-se uma string."},
        validate=[validate.Length(
            min=14,
            error="O cnpj deve ter no mínimo 14 caracteres."
        ), ValidateCPFCNPJ().validate]
    )


def validate_create_company_schema(name: str, cnpj: str):
    try:
        EditCompanySchema().load({
            "name": name,
            "cnpj": cnpj
        })

        print("Validação feita com sucesso")
    except ValidationError as error:
        pprint(error.messages)