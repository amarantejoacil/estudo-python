#!/usr/local/bin/python3
# -*- coding: ISO-8859-1 -*-

# with gerencia abertura e fechado da funcao open
# mais simples e seguro...

"""
modos open
r = leitura
w = escrita, substitui o arquivo existente
h = escrita, retorna erro se o arquivo ja existe
a = escrita, insere novos dados no final da informacao
b = modo binario
t = modo padrao
+ = atualizado tanto leitura e escrita
"""


with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            saida.write('Nome: {}, Idade:{}\n'.format(*pessoa))
            # print(, file == saida)


# verifica se o arquivo foi fechado corretamente
if arquivo.closed:
    print('arquivo foi fechado')

if saida.closed:
    print('o arquivo saida foi fechado')
