entrada = input()
matriz = []

def fazMatriz(x):
    retorno = []
    for i in range(x):
        retorno.append([3]*x)
    return retorno


while entrada.isdigit():

    entrada = int(entrada)

    if 3 <= entrada <= 70:

        aux = fazMatriz(entrada)

        for i in range(entrada):
            aux[i][i] = 1

        for i in range(entrada):
            aux[i][entrada-i-1] = 2

        matriz.append(aux)

        entrada = input()

for o in matriz:
    for i in o:
        for j in i:
            print(j, end='')
        print()