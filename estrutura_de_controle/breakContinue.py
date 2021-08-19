

# continue interrompe aquela acao e vai para proxima
# toda vez que achar um numero par ele para e vai para proxima
# ou seja ira imprimir todos os numeros impar
# nao interrompe o if e sim o for
for x in range(1, 11):
    if x % 2 == 0:
        continue
    print(x)

# interrompe o laco e vai para proxima instrucoes do programa
for y in range(1, 11):
    if y == 5:
        break
    print(y)

# continua executando depois do break
print('fim')
print('fim')
print('fim')
