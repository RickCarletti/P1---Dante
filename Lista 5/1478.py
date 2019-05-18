def fazMatriz(x):
    retorno = []
    for i in range(x):
        retorno.append([1]*x)
    return retorno


entrada = int(input())

resultado = []

while 0 < entrada <= 100:

    matriz = fazMatriz(entrada)

    for linha in range(entrada):
        for coluna in range(entrada):
            if linha == coluna:

                cont = 1
                for i in range(coluna+1, entrada):
                    matriz[linha][i] += cont
                    cont += 1

                cont = 1
                for i in range(coluna-1, -1, -1):
                    matriz[linha][i] += cont
                    cont += 1

    resultado.append(matriz)

    entrada = int(input())

for matriz in resultado:
    for linha in matriz:
       string = ""
       for index, coluna in enumerate(linha):

           qtdCaracteres = len(str(coluna))

           if index == 0:
               for i in range(qtdCaracteres, 3):
                   string += " "
               string += str(coluna)

           else:
               for i in range(qtdCaracteres, 4):
                   string += " "
               string += str(coluna)

       print(string)

    print()
