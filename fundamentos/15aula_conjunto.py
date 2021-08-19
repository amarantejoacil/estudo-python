""" lista VS conjuntos
  Lista 
  - sao estrutura indexada, 0,1,2,3,4 ... ou seja ela tem posicoes
  - aceita varios valores iguais... repetidos
  - por padrao ela segue a ordem de inserção


  Conjunto
    - não é indexado
    - nao aceita valores repetidos..
    - nao garante ordem de inserção

    a = [1,2,3] = LISTA
    a = (1,2,3) = TUPLA
    a = {1,2,3} = CONJUNTO
"""
a = {1, 2, 3}
# print(type(a))  # retorna set
# a[0] --- nao funciona pois nao tem index
a = set('coddddd3r')  # unifica todos os ddddd em um d.. nao aceita repeticoes
print(a)  # retorna as letras separadas em ordem aleatoria

print('3' in a, 4 not in a)  # retorna true true


# retorna true, os valores repetidos sao unificados e nao importa a ordem
print({1, 2, 3} == {3, 2, 1, 3})


# UNIAO
c1 = {1, 2}
c2 = {2, 3}
print('RESULTADO UNIAO')
print(c1.union(c2))
# gera novo conjunto resultado 1,2,3 ... ele unifico o 2
# porem nao atualiza.. para atualisar seria o exemplo abaixo
# c1.update(c2) resultado seria atualizado para 1,2,3


# INTERCESSAO
# o que sao comuns aos dois conjuntos
print('RESULTADO INTERCESSAO')
print(c1.intersection(c2))

{1, 2, 3} - {2}
# resultado é retira o 2, 1,2... porem n existe soma.
