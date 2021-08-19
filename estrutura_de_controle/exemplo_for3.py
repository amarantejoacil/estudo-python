

# percorrer dicionario
produto = {'nome': 'caneta', 'preco': 15.44, 'importada': True,
           'estoque': 983}

# percorre chave ou id = FORMATO 1
for chave in produto:
    print(chave)


# percorre chave ou id = FORMATO 2
for chave in produto.keys():
    print(chave)


# percorre valores
for valor in produto.values():
    print(valor)

# percorr chave e valores juntos
for chave, valor in produto.items():
    print(chave, valor)
