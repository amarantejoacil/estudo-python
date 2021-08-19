#!/usr/local/bin/python3

"""


"""


def impost_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, faltor_mult=1):
    return 0.11 * faltor_mult if explosivo else 0


def calc_preco_final(preco_bruto, calc_imposto, *parms):
    return preco_bruto + preco_bruto * calc_imposto(*parms)


preco_final = calc_preco_final(150, impost_x, True)
preco_final = calc_preco_final(preco_final, imposto_y, 1.5)
print(f'Preco final RS {preco_final}')
