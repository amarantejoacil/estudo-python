# -*- coding: utf-8 -*-
# criando funcao


import math

# nao retorna nada.


def circulo(raio):
    print('Area do circulo', math.pi * raio ** 2)


if __name__ == '__main__':
    raio = input('Informe o radio: ')
    circulo(raio)
