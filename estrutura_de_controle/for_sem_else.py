PALAVRA_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = [
    'Joao gosta de futebol e politica',
    'Maria foi a praia ontem'
]

for texto in textos:
    existe = False
    for palavra in texto.lower().split():
        if palavra in PALAVRA_PROIBIDAS:
            print('texto negado', palavra)
            existe = True
            break

    if existe == True:
        print('palavra autorizado', texto)
