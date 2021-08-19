

lista = []
# list é dinamina e heterogenico, aceita varios tipos... string, int, float
# dir(lista) retorna o tipo
# help(list)  te mostra como utilizar a list
lista.append(1)  # adiciona 1
lista.append(5)  # adiciona o 5

print(lista)

nova_lista = [1, 5, 'ana', 'bia']  # lista com varios tipos
print(nova_lista)

nova_lista.remove(5)
# remove o numero 5, nao confudir com posicao 5. retorna [1, 'ana', 'bia']
print(nova_lista)


nova_lista.reverse()
print(nova_lista)  # reverte a posicao retorna ['bia', 'ana', 1]

# sempre começa o index(posicao) do 0
lista_exemplo = [1, 5, 'ana', 'guilherme', 3.1415]
print(lista_exemplo.index('guilherme'))
print(1 in lista)           # retorna true... existe 1 na lista?
print('rebeca' in lista)    # retorna false...nao existe rebeca na lista
print('Pedro' not in lista)  # retorna true, pedro nao existe.
print(lista_exemplo[2])     # retorna posicao 2... contantdo apartir do 0


lista_nome = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista_nome[1:3])  # acessando intervalo de informacao
del lista_nome[2]
print(lista_nome)  # deleta posicao 2 contando do 0
