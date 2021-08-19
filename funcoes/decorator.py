#!/usr/local/bin/python3
"""


"""


def log(function):
    def decorator(*parm_seq, **parm_nomeado):
        print(f'Inicio da chamada da funcao: {function.__name__}')
        print(f'args_sequencial: {parm_seq}')
        print(f'args_nomeado: {parm_nomeado}')
        resultado = function(*parm_seq, **parm_nomeado)
        print(f'resultado da chamada {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == '__main__':
    print(soma(5, 7))
    print(sub(5, y=7))
