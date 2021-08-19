#!/usr/local/bin/python3
# -*- coding: latin1 -*-
import csv
# import urllib.request
#from urllib import request


# funciona mas nao sei como kkk
import urllib2


def read(url):
    req = urllib2.Request(url)
    resposta = urllib2.urlopen(req)
    for cidade in csv.reader(resposta):
        print('Cidade: {}, Cidade: {}'.format(cidade[8], cidade[3]))


"""


def read(url):
    with request.urlopen(url) as entrada:
        print('baixando csv')
        dados = entrada.read().decode('latin1')
        print('download finalizado')
        for cidade in csv.reader(dados.splitlines()):
            print('a')
            # print(f'{cidade[8]}: {cidade[3]}')
"""

if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
