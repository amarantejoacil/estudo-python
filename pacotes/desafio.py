from app.utils.gerador import novo_nome
from app.negocio import nome_existe
from app.negocio.backend import add_nome

# def novo_nome():


def main():
    while True:
        nome = novo_nome()
        if not nome_existe(nome):
            add_nome(nome)
            break
    print(nome)


main()
