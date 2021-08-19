#!/usr/local/bin/python3

# recomendavel que utilize dessa forma (Leitura Streaming)
# pois é mais performatico
# abre arquivos
arquivo = open('pessoas.csv')

for registro in arquivo:
    # obs. nesse formato ele deixa 2 espaco entre linha...
    # ira resolver na proxima aula
    print('Nome: {}, Idade:{}'.format(*registro.split(',')))
arquivo.close
