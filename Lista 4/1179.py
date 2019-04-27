#listaDeEntradas = [1, 3, 4, -4, 2, 3, 8, 2, 5, -7, 54, 76, 79, 23, 98]

listaPar, listaImpar = [], []
contPar, contImpar = 0, 0
despejo = 5
count = 0

for i in range(15):
    entrada = int(input())

    if (entrada % 2 == 0): listaPar.append(entrada)
    else: listaImpar.append(entrada)

    if (len(listaPar) == despejo):
        for index, par in enumerate(listaPar):
            print("par[" + str(index) + "] = " + str(par))
        listaPar.clear()

    if (len(listaImpar) == despejo):
        for index, impar in enumerate(listaImpar):
            print("impar[" + str(index) + "] = " + str(impar))
        listaImpar.clear()

    if count == 14:
        for index, impar in enumerate(listaImpar):
            print("impar[" + str(index) + "] = " + str(impar))
        listaImpar.clear()

        for index, par in enumerate(listaPar):
            print("par[" + str(index) + "] = " + str(par))
        listaPar.clear()
    count += 1




'''
1
3
4
-4
2
3
8
2
5
-7
54
76
789
23
98

'''
