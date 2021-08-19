
# tipo dict dicionario
pessoa = {'nome': 'Prof. Ana', 'idade': 38, 'cursos': ['ingles', 'portugues']}

print(pessoa)
print(pessoa['nome'])  # result prof. ana - acessando lista
print(pessoa['cursos'][0])

# recupera as chave retorna nome idade e curso
pessoa.keys

# retorna os valores prof. ana, 38, ingles e portugues
pessoa.values

# retorna chave e valor
pessoa.items()

# retorna idade
print(pessoa.get('idade'))


# manipular os dados de dicionario
print('-------------------------exemplo 02-------------------------')
pessoa2 = {'nome': 'Prof. Roberto', 'idade': 43, 'cursos': ['React', 'Python']}
print(pessoa2)

pessoa2['idade'] = 44  # atualiza valor da idade
pessoa2['cursos'].append('Angular')  # adicionar o curso angular
# pessoa2.pop('idade') - le o valor idade e retira da lista

# atualiza os valores e incluir novos item na lista tb
pessoa2.update({'idade': 40, 'sexo': 'Masculino'})
del pessoa2['cursos']  # exclui o item curso
# pessoa2.clear()  # limpra todo dicionario retornado apenas {}
print(pessoa2)
