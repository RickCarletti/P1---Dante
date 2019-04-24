def ordenaSimples(vetor, sen):
    tamanhoVetor = len(vetor)-1
    ordenando = True
    while ordenando:
        ordenando = False
        for i in range(tamanhoVetor):
            if sen:
                if vetor[i] > vetor[i+1]:
                    vetor[i], vetor[i+1] = vetor[i+1],vetor[i]
                    ordenando = True
            else:
                if vetor[i] < vetor[i + 1]:
                    vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                    ordenando = True
    return vetor

lista = list(map(int, input().split()))
listaInt = []
for i in range(len(lista)): listaInt.append(int(lista[i]))
listaOrdenada = ordenaSimples(listaInt, True)

for x in range(len(listaOrdenada)): print(listaOrdenada[x])
print("")
for x in range(len(lista)): print(lista[x])