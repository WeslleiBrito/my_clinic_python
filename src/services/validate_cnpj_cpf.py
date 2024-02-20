class ValidateCPFCNPJ:
    def validate(self, number: str) -> bool:
        number = ''.join(filter(str.isdigit, number))

        if len(number) == 11:
            if not number.isdigit():
                raise ValueError("CPF inválido.")

            amount = 0
            for i in range(9):
                amount += int(number[i]) * (10 - i)

            rest = 11 - (amount % 11)
            if rest in {10, 11}:
                rest = 0

            if rest != int(number[9]):
                raise ValueError("CPF inválido.")

            amount = 0
            for i in range(10):
                amount += int(number[i]) * (11 - i)

            rest = 11 - (amount % 11)
            if rest in {10, 11}:
                rest = 0

            if rest != int(number[10]):
                raise ValueError("CPF inválido.")

        elif len(number) == 14:
            if not number.isdigit():
                raise ValueError("CNPJ inválido")

            weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            amount = 0
            for i in range(12):
                amount += int(number[i]) * weight[i]

            rest = amount % 11
            if rest < 2:
                if int(number[12]) != 0:
                    raise ValueError("CNPJ inválido")
            else:
                if int(number[12]) != 11 - rest:
                    raise ValueError("CNPJ inválido")

            amount = 0
            weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            for i in range(13):
                amount += int(number[i]) * weight[i]

            rest = amount % 11
            if rest < 2:
                if int(number[13]) != 0:
                    raise ValueError("CNPJ inválido")
            else:
                if int(number[13]) != 11 - rest:
                    raise ValueError("CNPJ inválido")

        else:
            raise ValueError("Número inválido: deve ter 11 dígitos para CPF ou 14 dígitos para CNPJ")

        return True