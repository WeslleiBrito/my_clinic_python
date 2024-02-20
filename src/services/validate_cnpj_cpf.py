from typing import Union


class ValidateCPFCNPJ:
    @staticmethod
    def validate(number: str) -> dict[str, Union[bool, str]]:
        number = ''.join(filter(str.isdigit, number))

        if len(number) == 11:
            if not number.isdigit():
                return {
                    "status": False,
                    "message": "CPF inválido"
                }

            amount = 0
            for i in range(9):
                amount += int(number[i]) * (10 - i)

            rest = 11 - (amount % 11)
            if rest in {10, 11}:
                rest = 0

            if rest != int(number[9]):
                return {
                    "status": False,
                    "message": "CPF inválido"
                }

            amount = 0
            for i in range(10):
                amount += int(number[i]) * (11 - i)

            rest = 11 - (amount % 11)
            if rest in {10, 11}:
                rest = 0

            if rest != int(number[10]):
                return {
                    "status": False,
                    "message": "CPF inválido"
                }

        elif len(number) == 14:
            if not number.isdigit():
                return {
                    "status": False,
                    "message": "CPF inválido"
                }

            weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            amount = 0
            for i in range(12):
                amount += int(number[i]) * weight[i]

            rest = amount % 11
            if rest < 2:
                if int(number[12]) != 0:
                    return {
                        "status": False,
                        "message": "CNPJ inválido"
                    }
            else:
                if int(number[12]) != 11 - rest:
                    return {
                        "status": False,
                        "message": "CNPJ inválido"
                    }

            amount = 0
            weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            for i in range(13):
                amount += int(number[i]) * weight[i]

            rest = amount % 11
            if rest < 2:
                if int(number[13]) != 0:
                    return {
                        "status": False,
                        "message": "CNPJ inválido"
                    }
            else:
                if int(number[13]) != 11 - rest:
                    return {
                        "status": False,
                        "message": "CNPJ inválido"
                    }

        else:
            message: str = "O cpf deve ter no mínimo 11 caracteres." if len(number) < 11 else "O CNPJ deve ter no mínimo 14 caracteres."
            return {
                "status": False,
                "message": message
            }
        return {
            "status": True,
            "message": "CNPJ inválido"
        }
