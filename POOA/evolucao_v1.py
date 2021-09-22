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


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()


    print(f'Humanos.especie1: {Humano.especie}')
    print(f'jose.especie2: {jose.especie}')
    print(f'grokn.especie3: {grokn.especie}')