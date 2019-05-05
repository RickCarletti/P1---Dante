quantidadeValores = int(input())
lista = []
aux = []
listaResultado = []

for i in range(quantidadeValores):
    lista.append(int(input()))

for i in lista:
   if i not in aux:
       aux.append(i)
       listaResultado.append([i, lista.count(i)])

listaResultado.sort()

for i in listaResultado:
    print(str(i[0]) + " aparece " + str(i[1]) +" vez(es)")