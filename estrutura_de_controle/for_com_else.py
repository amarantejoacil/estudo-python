PALAVRA_PROIBIDAS = ('futebol', 'religiao', 'politica')
textos = [
    'Joao gosta de futebol e politica',
    'Maria foi a praia ontem'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRA_PROIBIDAS:
            print('texto negado', palavra)
            break
    else:
        print('palavra autorizado', texto)
