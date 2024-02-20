import flet as ft
from src.business.company_business import CompaniesBusiness


def main(page):
    def send(e):
        class_business = CompaniesBusiness()
        class_business.create_company(name.value, cnpj.value)
        result = class_business.findCompanyAll()
        for r in result:
            print(r)

    name = ft.TextField(label="Nome da empresa")
    cnpj = ft.TextField(label="CNPJ")

    page.add(
        name,
        cnpj,
        ft.ElevatedButton("Enviar", on_click=send)
    )


ft.app(target=main)
