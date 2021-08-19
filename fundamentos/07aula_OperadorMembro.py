
# operadores membro
lista = [1, 2, 3, 'ana', 'joao']
print(2 in lista)  # true contem 2 na lista?
# se nao esta presente na lista, exemplo: ana nao esta presente na lista
print('ana' not in lista)


# operadores identidade
# exemplo com numeros inteiros
x = 3
y = x
z = 3

print('inteirooooooooo')
print(x is y)  # true
print(y is x)  # true
print(x is not z)  # false

# exemplo com lista
lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print('listaaaaaaaaaaa')
print(lista_a is lista_b)  # true
print(lista_b is lista_c)
# false, pois apesar de ter os mesmo valores sao alocados em memorias diferentes

print(lista_a is not lista_c)  # true,confirma que nao sao as mesma lista
