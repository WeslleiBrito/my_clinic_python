import flet as ft
from src.business.company_business import CompaniesBusiness


def main(page: ft.Page):
    def send(e):

        try:

            class_business = CompaniesBusiness()
            class_business.create_company(name.value, cnpj.value)
            result = class_business.findCompanyAll()
            for r in result:
                print(r)
        except ValueError as error:
            print("Eu capturei")
            if error.args[0]["name"]:
                name.error_text = error.args[0]["name"]

            if error.args[0]["cnpj"]:
                cnpj.error_text = error.args[0]["cnpj"]

            page.update()
            print(error.args[0])

    name = ft.TextField(label="Nome da empresa")
    cnpj = ft.TextField(label="CNPJ OU CPF")

    page.add(
        name,
        cnpj,

        ft.ElevatedButton("Enviar", on_click=send)
    )


ft.app(target=main)
