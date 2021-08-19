

# resultado = (posicao false, posicao true) [condicao]
# resultado = (sou verdadeiro, sou falso) [ 2 > 1]
# resultado = sou falso
# exemplo


# ternario 1
tempohoje = False
print('Vai chover hoje' + (' não', ' sim')[tempohoje])

# ternario 2

tempoFrio = True
print('a temperatura esta  ' + ('-5c' if tempoFrio else '37c'))
