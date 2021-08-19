"""
generation - consome menos memoria que o promprehension pois gera de acordo
sob a demandas. é necessario que vc va pedindo o proximo item


diferente do comprehension que gera toda a lista completa
OBs. sempre analisa se compensa usar ou não.
"""


generator = (i ** 2 for i in range(11) if i % 2 == 0)
print(next(generator))  # resultado = 0
print(next(generator))  # resultado = 4
print(next(generator))  # resultado = 16
print(next(generator))  # resultado = 36
print(next(generator))  # resultado = 64
# print(next(generator)) #resultado = ERRO!

"""
Teste que verificar o tamanho de consumo de memoria... executar no python

a = [i * 2 for i in range(1000) if i % 2 == 0]
import sys
sys.getsizeof(a)


b = [i * 2 for i in range(1000) if i % 2 == 0]
import sys
sys.getsizeof(b)



"""
