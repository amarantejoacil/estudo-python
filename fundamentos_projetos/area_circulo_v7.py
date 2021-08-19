# -*- coding: utf-8 -*-
# criando funcao


import math
import sys

# estrutura if else

a = 1


def circulo(raio):
    return math.pi * raio ** 2


if __name__ == '__main__':
    if a == 1:
        print('exec se for true')
        sys.exit(1)  # finaliza aqui nao executa nada em baixo
        print('nao executa')
    else:
        print('executa se for falsefalse')
