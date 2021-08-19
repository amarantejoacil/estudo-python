#!/usr/local/bin/python3


# abre arquivos
arquivo = open('pessoas.csv')

# le arquivo e armazena na variavel dados
dados = arquivo.read()


# fecha arquivo
arquivo.close()

# splitlines divide as linhas
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

    # print(registro.split(','))
