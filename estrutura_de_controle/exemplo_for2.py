
# como percorrer letras de uma string
palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=",")
print('fim')


# percorrendo lista
aprovados = ['joao', 'maria', 'zezinho', 'carlos']
for nome in aprovados:
    print(nome)

# enumerando a lista...
for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)


# imprimindo dias da semana
dias_semana = ('domingo', 'segunda', 'terca',
               'quarta', 'quinta', 'sexta', 'sabado')
for dia in dias_semana:
    print(f'Hoje e dia {dia}')
