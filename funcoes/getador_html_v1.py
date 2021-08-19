#!/usr/local/bin/python3

"""
def tag_bloco(texto,tipo_pessoa = 'J') obs. tipo_pessoa é um 
valor default como J
se nao receber nenhum valor

"""


def tag_bloco(texto, classe='success', inline=False):
    # tag recebe span se for inline, se nao div
    # executa IF , se nao executa else
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('parametro posicional', 'info', True))
    print(tag_bloco('parametro nomeado', inline=True))
