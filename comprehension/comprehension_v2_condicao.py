# [ expressao, for item in list ,if condicional ]
# [ excpressao , for , if]
dobros = [item * 2 for item in range(11) if item % 2 == 0]

print(dobros)

# versao normal

dobro = []
for i in range(11):
    if i % 2 == 0:
        dobro.append(i * 2)
print(dobro)
