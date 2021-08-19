# -*- coding: utf-8 -*-

# modelo com retorno
def imprimir_conceito(nota):
    if nota >= 9.1 and nota <= 10:
        return('Seu conceito e: A',)
    elif nota >= 8.1 and nota <= 9:
        return('Seu conceito e: A-')
    elif nota < 9 and nota > 0:
        return('Sue conceito e: B')
    else:
        return('nota invalidade')


if __name__ == '__main__':
    valor_informador = input('digite sua nota: ')
    conceito = imprimir_conceito(valor_informador)
    print(conceito)


"""   feito por min
def imprimir_conceito(nota, nome):
    if nota >= 9.1 and nota <= 10:
        print('Seu conceito e: A', nome)
    elif nota >= 8.1 and nota <= 9:
        print('Seu conceito e: A-', nome)
    elif nota < 9 and nota > 0:
        print('Sue conceito e: B', nome)
    else:
        print('nota invalidade')


nota = input('Digite sua nota: ')
nome = raw_input('Digite seu nome: ')

imprimir_conceito(nota, nome)

"""
