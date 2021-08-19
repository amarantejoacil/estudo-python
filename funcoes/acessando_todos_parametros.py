#!/usr/local/bin/python3
"""

sempre passa primeiro os parm posicional depois os nomeados


"""


def todos_parametros(*args, **kwargs):
    print(f'args -> {args}')
    print(f'kwargs -> {kwargs}')
    print('-----------------------------------')


todos_parametros('a', 'b', 'c')  # args

# args e kwargs separados
todos_parametros(1, 2, 3, explosivo=True, Valor=12.33)

# args e kwargs separados
todos_parametros('ana', False, [1, 2, 3], tamanho='M', explosivo=True)

# erro pq passou kwargs primeiro...
todos_parametros(explosivo=True, 'ana')
# jeito correto = todos_parametros('ana',explosivo=True)
