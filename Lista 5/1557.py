def fazMatriz(x):
    retorno = []
    for i in range(x):
        retorno.append([1]*x)
    return retorno


entrada = int(input())

resultado = []

while 0 < entrada <= 15:

    matriz = fazMatriz(entrada)

    for linha in range(entrada):

        if not linha == 0:
            x = matriz[linha-1][0]
            matriz[linha][0] = x * 2

        for coluna in range(1, entrada):
            x = matriz[linha][coluna-1]
            matriz[linha][coluna] = x * 2

    resultado.append(matriz)

    entrada = int(input())

for matriz in resultado:
    for linha in matriz:
       string = ""
       for index, coluna in enumerate(linha):

           qtdCaracteres = len(str(coluna))

           if index == 0:
               for i in range(qtdCaracteres, 1):
                   string += " "
               string += str(coluna)

           else:
               for i in range(qtdCaracteres, 2):
                   string += " "
               string += str(coluna)

       print(string)

    print()
