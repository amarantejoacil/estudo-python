#!/usr/local/bin/python3
"""


callable = verifica se é uma funcao e executa ela..
podendo chamar uma funcao dentro de funcao
"""


def bomdia():
    print('bom dia')


def boatarde():
    print('boa tarde')


def executar(funcao):
    if callable(funcao):
        funcao()


executar(bomdia)
