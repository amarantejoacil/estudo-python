#!/usr/local/bin/python3
"""packing = empacotamento
unpacking = desmpacotamento

"""


def resultado_f1(**classificacao):
    for posicao, piloto in classificacao.items():
        print(f'{posicao} -> {piloto}')


resultado_f1(primeiro='L. Hamilton',
             segundo='Jose',
             terceiro='Maria')
