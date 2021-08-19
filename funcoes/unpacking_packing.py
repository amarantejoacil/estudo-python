#!/usr/local/bin/python3
"""packing = empacotamento
unpacking = desmpacotamento

"""


def soma2(a, b):
    return a + b


def soma3(a, b, c):
    return a + b + c


def soma_n(*numeros_entrada):
    soma = 0
    for n in numeros_entrada:
        soma += n
    return soma


print(soma2(2, 4))
print(soma3(2, 4, 6))


# gera um tupla e EMPACOTA packing
print(soma_n(1, 1, 1, 1, 1, 1, 1, 1, 1, 1,))


# unpacking da tupla - DESEMPACOTE
nums_tupla = (1, 2, 3)
print(soma3(*nums_tupla))


# unpacking da lista - DESEMPACOTE
nums_lista = [1, 2, 3]
print(soma3(*nums_lista))
