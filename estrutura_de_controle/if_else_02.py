# -*- coding: utf-8 -*-

# modelo com retorno
def faixa_etaria(idade):
    if 0 < idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    else:
        return 'Idade invalida'

#range = intervalo


if __name__ == '__main__':
    for idade in (17, 37, 87, -2):
        print(f'{idade}: {faixa_etaria(idade)}')
