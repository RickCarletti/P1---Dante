quantidadeValores = int(input())
lista = {}

for i in range(quantidadeValores):
    entrada = int(input())

    if entrada in lista: lista[entrada] += 1
    else: lista[entrada] = 1

chaves = lista.keys()
chaves = sorted(chaves)

for i in chaves:
    print(str(i) + " aparece " + str(lista[i]) +" vez(es)")