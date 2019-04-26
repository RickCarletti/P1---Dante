listaDeEntrada = [[0,25], [25,50], [50,75], [75,100]]
maiorQueMenorQue = []
for i in range(len(listaDeEntrada[0])): maiorQueMenorQue.append(False)

def achaValor(listaDeValores, valor):
    indexI = 0
    indexJ = 0
    if valor < 0 and 100 > valor: return "Fora de intervalo"
    for i in range(len(listaDeValores)):
        indexI = i
        maiorQueMenorQue.clear()
        for j in range(len(listaDeValores[i])):
            indexJ = j
            if valor - listaDeValores[i][j] >= 0:
                if indexI == (len(listaDeValores)-1) and indexJ == (len(listaDeValores[i])-1):
                    maiorQueMenorQue.append(False)
                else: maiorQueMenorQue.append(True)
            else:
                maiorQueMenorQue.append(False)
        print(indexJ)
        print(len(listaDeValores)-1)
        print(maiorQueMenorQue)
        if not all(i == True for i in maiorQueMenorQue): return listaDeValores[i]
while True:
    entrada = float(input())
    res = achaValor(listaDeEntrada, entrada)
    print(res)