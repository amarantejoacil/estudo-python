#!/usr/local/bin/python3

# with gerencia abertura e fechado da funcao open
# mais simples e seguro...
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade:{}'.format(*registro.strip().split(',')))


# verifica se o arquivo foi fechado corretamente
if arquivo.closed:
    print('arquivo foi fechado')
