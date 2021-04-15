class Data:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return(f'{self.dia}/{self.mes}/{self.ano}')


d1 = Data(5, 1, 2021)
#d1.dia = 5
#d1.mes = 1
#d1.ano = 2021

print(d1)


d2 = Data(1, 2, 2023)
#d2.dia = 1
#d2.mes = 2
#d2.ano = 2023

print(d2)
