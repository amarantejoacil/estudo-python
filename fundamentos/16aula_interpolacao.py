from string import Template
nome, idade, altura = 'Ana', 30, 1.80

# %s substituir elementos tipo string
# %d substituir elementos tipo inteiro
# %f substituir elementos tipo float, %.2f limita a 2 casa decimal

# exemplo 1 - forma mais antiga
print('nome: %s e sua idade é %d , tendo %.2f' % (nome, idade, altura))
# resultado = nome: Ana e sua idade é 30 , tendo 1.80


# exemplo 2 - antes do python 3
print('Nome: {0} Idade: {1} Altura {2}'.format(nome, idade, altura))

# MAIS PRATICA
# exemplo 3 disponivel da versao 3.6 - forma mais pratica
print(f'Nome: {nome} Idade {idade} Altura {altura} exemplo calculo {2+2}')


# exemplo 4 - precisa do import e do template
s = Template('Nome: $n Idade: $i')
print(s.substitute(n=nome, i=idade))
