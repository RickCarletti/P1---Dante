entrada = []
for i in range(20):
    entrada.append(int(input()))

def troca(vetor):
    res = []
    for i in range(len(vetor)-1, -1, -1):
        res.append(vetor[i])
    return res

saida = troca(entrada)

for index, i in enumerate(saida):
    print("N[" + str(index) + "] = " + str(i))