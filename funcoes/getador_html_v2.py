#!/usr/local/bin/python3

"""
''.join = unifica o resuldo da interpolacao com for dentro de uma string vazia



"""


def tag_lista(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


print(tag_lista('ana', 'maria', 'joao'))
