#!/usr/local/bin/python3

# finally sempre sera executato independente se teve erro ou nao
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade:{}'.format(*registro.strip().split(',')))
finally:
    arquivo.close()

# verifica se o arquivo foi fechado corretamente
if arquivo.closed:
    print('arquivo foi fechado')


""""

# finally sempre sera executato independente se teve erro ou nao
try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade:{}'.format(*registro.strip().split(',')))
except IndexError:  # forca continuar o processo mesmo com erro... CUIDADOOOO
    pass
finally:
    arquivo.close()

# verifica se o arquivo foi fechado corretamente
if arquivo.closed:
    print('arquivo foi fechado')


"""
