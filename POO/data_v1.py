class Data:
    # construtor
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


"""metodo que faz retorna string"""


def __str__(self):
    return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2019)
# d1.dia=5
# d1.mes=12
# d1.ano=1999
print(d1)

d2 = Data(20, '01', 2012)
# d2.dia = 20
# d2.mes = '01'
# d2.ano = 2012
print(d2)
