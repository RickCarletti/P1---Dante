matriz = []

def fazMatriz(x):
    retorno = []
    for i in range(x):
        retorno.append([3]*x)
    return retorno


while True:
    try:
        entrada = input()
        entrada = int(entrada)
    except:
        break

    if 3 <= entrada < 70:

        aux = fazMatriz(entrada)

        for i in range(entrada):
            aux[i][i] = 1

        for i in range(entrada):
            aux[i][entrada-i-1] = 2

        matriz.append(aux)

for objeto in matriz:
    for linha in objeto:
        for coluna in linha:
            print(coluna, end='')
        print()