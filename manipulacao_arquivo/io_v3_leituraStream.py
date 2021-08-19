#!/usr/local/bin/python3

# recomendavel que utilize dessa forma (Leitura Streaming)
# pois E mais performatico
# abre arquivos
arquivo = open('pessoas.csv')

for registro in arquivo:
    # obs. nesse formato ele deixa 2 espaco entre linha...
    # ira resolver na proxima aula
    print('Nome: {}, Idade:{}'.format(*registro.strip().split(',')))
arquivo.close

# STRIP REMOVE OS ESPACOS LATERAIS
# SE FOR PASSADO PARAMETRO EXEMPLO 0, REMOVE O ZERO E OS ESPACOS
teste_strip = '     00011 002220  0330     '
print(teste_strip.strip())  # retira espeacos laterais
print(teste_strip.strip().strip('0'))  # alem dos espacos lateris , retira os 0
