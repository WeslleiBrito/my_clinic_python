import flet as ft
from src.business.company_business import CompaniesBusiness


def main(page: ft.Page):
    page.title = "Empresas"

    lv = ft.ListView(
        expand=1,
        spacing=10,
        padding=20
    )

    companies = CompaniesBusiness()
    list_companies = companies.findCompanyAll()

    rows = []

    def on_change_check(id_company):
        def on_change(e=ft.ControlEvent):
            print(id_company)

        return on_change

    for company in list_companies:
        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Checkbox(on_change=on_change_check(id_company=company["id"]))),
                ft.DataCell(ft.Text(company["name"])),
                ft.DataCell(ft.Text(company["cnpj"]))
            ]
        )

        rows.append(row)

    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Checkbox()),
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("CNPJ"))
            ],
            rows=rows
        ),
        ft.Checkbox(label="Teste", label_position=ft.LabelPosition.RIGHT)
    )


ft.app(target=main)
