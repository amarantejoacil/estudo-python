from decimal import *

# tipos inteiros e float
# is_integer() verificar se e inteiro e retorna true e false

getcontext().prec = 6  # obriga a trabalhar com 6 casa
print(Decimal(1)/Decimal(7))  # transforma em decimal

print(2.5.is_integer())  # retorna false pois e float

print(5.0.is_integer())  # retorna true pois e inteiro

a = 1.1
b = 2.2


print(a+b)  # resultado = 3.3000000000000003

getcontext().prec = 2
print(Decimal(a)+Decimal(b))  # resultado  = 3.3
