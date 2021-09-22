#!/usr/local/bin/python3


class Humano:
    especie = 'Homo Sapiens'

    #atributo de instância
    def __init__(self, nome):
        self.nome = nome

    # atributo de classe
    def das_cavernas(self):
        self.especie = 'Homo Bla Bla Bla'
        return self

    # metodo estático
    @staticmethod
    def especies():
        adjetivos = ('01','02','03','04')
        return ('Austrapoliteco',) + tuple(f'homo {adj}' for adj in adjetivos)

    
    #metodo de class
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especie()[-1]


class Neanderthal(Humano):
    especie = Humano.especie()[-2]


class HomoSapiens(Humano):
    especie = Humano.especie()[-1]


if __name__ == '__main__':
  jose = HomoSapiens('José')
  grokn = Neanderthal('Grokn')
  print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especie())}' )