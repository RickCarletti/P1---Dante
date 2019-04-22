notas = []
qtdeNotas = 2
resultado = 0
while len(notas) is not qtdeNotas:
    entrada = float(input())
    if entrada >= 0 and entrada <= 10:
        notas.append(entrada)
    else: print("nota invalida")
for x in range(len(notas)): resultado += notas[x]
resultado = resultado / len(notas)
print("media = ", "%.2f" % resultado)