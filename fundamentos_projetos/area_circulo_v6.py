# -*- coding: utf-8 -*-
# criando funcao


import math

# funcao com retorn


def circulo(raio):
    return math.pi * raio ** 2


if __name__ == '__main__':
    raio = input('Informe o radio: ')
    area = circulo(raio)
    print('area: ', area)
