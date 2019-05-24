'''
41805
99934
39127
23659
'''

matring = []

for i in range(4):
    aux = input()
    linha = []
    for c in aux:
        linha.append(int(c))
    matring.append(linha)

resultado = []

F = L = Mi = ''

for linha in matring:

    F += str(linha[0])
    L += str(linha[-1])


for i in range(1, len(matring[0])-1):
    Mi = ''
    for c in matring:
        Mi += str(c[i])

    resultado.append((int(F) * int(Mi) + int(L)) % 257)

for c in resultado:
    print(str(chr(c)), end='')