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
    tamMax = len(str(matriz[-1][-1]))+1
    for linha in matriz:
        for index, coluna in enumerate(linha):

            tam = len(str(coluna))

            frase = ""

            if index == 0:
                frase = " " * (tamMax - tam - 1)
            else:
                frase = " " * (tamMax - tam)

            print(frase + str(coluna), end='')

        print()
    print()