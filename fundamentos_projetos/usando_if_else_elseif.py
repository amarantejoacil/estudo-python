# -*- coding: utf-8 -*-
# criando funcao


nota = 10

# identacao python com msg muita grande
# validar no pep8online
if nota == 10:
    print('este texto e bem grande, esse texto e bem grande kkkk k kkkkk k kkk kkk k kkk ' +
          str(nota))
else:
    print('teste')


if nota >= 9:
    print('parabens super aprovado')
elif nota >= 7:
    print('aprovado')
elif nota >= 5 and nota < 7:
    print('aluno de recuperacao')
else:
    print('aluno reprovado')
