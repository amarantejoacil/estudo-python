from random import randint

numero_informado = -1
numero_secreto = randint(0, 5)

while numero_informado != numero_secreto:
    numero_informado = int(input('Digite o numero informado: '))

print('numero informado {} foi encontrado'.format(numero_secreto))
