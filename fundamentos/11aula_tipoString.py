

# dir(srt) --- voce consegue ver todas as funcoes que pode utlilizar


# aspa simples dentro do texto
# 'marca d'agua' = errado

print("marca d'agua - exemplo aspa simples")
print('texto printando aspa dupla "aqui"')

texto_mutiplas_linhas = ' oi texto  quebra de linha\n aqui'
texto_mutiplas_linhas2 = """ texte 2 de multiplas linhas
texto linha dois
texto linha tres
"""

# tres aspa simples tambem consegue  ''' texto quebra aqui '''

print(texto_mutiplas_linhas)
print('-----------------------------------')
print(texto_mutiplas_linhas2)


nome = 'Ana Paula'

# sempre comeca com a posicao 0
print(nome[0])  # retorna A
print(nome[4:])  # retorna aparti da posicao 4 até o final
print(nome[:3])  # comeca no zero até posicao 2 , posicao 3 nao entra #ana
print(nome[2:5])  # com intervalo de posicao


frase = 'Python é uma linguagem excelente'
print('py' in frase)  # py existe dentro da var frase? false pois e Py
print('ing' in frase)  # ing existe dentro da var frase? true
print(len(frase))  # exibi a quantidade de caracter existente.
print(frase.lower())  # faz uma copia e deixa tudo minusculo
print(frase.upper())  # faz uma copia e deixa maisculo

# para mudar definitivamente deve ser realizado da seguinte maneira
frase = frase.upper()
print(frase)

print(frase.split())  # quebra os espaco
print(frase.split('E'))  # retirar toda letra é e quebra os espaco
