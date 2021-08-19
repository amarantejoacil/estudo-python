#!/usr/local/bin/python3

"""


"""


class Potencia:
    # calcula uma potencia especifica
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadradro = Potencia(2)
    cubo = Potencia(3)

    if callable(quadradro) and callable(cubo):
        print(f'3² -> {quadradro(3)}')
        print(f'5² -> {quadradro(5)}')
        print(f'3³ -> {cubo(3)}')
