from random import randint
""""
# executa as 10 posicoes e o else
from random import randint


for i in range(1, 11):
    print(i)
else:
    print('Fim')

# executa ate a 6 posicao e para e nao imprimi o else
for i in range(1, 11):
    if i == 6:
        break
    print(i)
else:
    print('Fim')
"""


def lancaDados():
    numero_digitado = input('Digite um numero entr 1 e 6:  ')
    numero_secreto = randint(1, 6)
    if numero_digitado > 0 and numero_digitado <= 6:
        for y in range(1, numero_digitado):
            if y % 2 != 0:
                continue
            print(y)
        else:
            if numero_digitado == numero_secreto:
                print('numero secreto {} foi encontrado'.format(numero_secreto))
            else:
                print('nao acertou o numero secreto')
    else:
        print('valor nao aceito!!!')


lancaDados()
