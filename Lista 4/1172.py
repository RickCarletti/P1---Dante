lista, saida = [], []

for i in range(10):
    lista.append(int(input()))

for i in lista:
    if i == 0:
        saida.append(1)
        #print(i)
    elif i < 0: saida.append(1)
    else: saida.append(i)

for index, i in enumerate(saida):
    print("X[" + str(index) + "] = " + str(i), end="\n")
print()