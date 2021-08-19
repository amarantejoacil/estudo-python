generator = (i ** 2 for i in range(11) if i % 2 == 0)

# no for nao precisa usar a funcao NEXT, ele entende a interacao a cada for.
for numero in generator:
    print(numero)
