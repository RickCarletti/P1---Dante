quantidadeValores = int(input())
lista, nVezes = [], []

for i in range(quantidadeValores):
    entrada = int(input())
    lista.append(entrada)
    if j in nVezes:
        nVezes += lista.count(i)
    print(str(i) + " Aaparece " + str(nVezes) + " vez(es)")

