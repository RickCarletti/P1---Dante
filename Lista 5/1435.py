dimensao = int(input())

def fazMatriz(x):
    retorno = []
    for i in range(x):
        retorno.append([0]*x)
    return retorno

resultado = []

while dimensao > 0:

    matriz = fazMatriz(dimensao)
    quadrante = 0

    while quadrante != dimensao:
        max = dimensao - quadrante
        min = quadrante
        for linha in range(min, max):
            for coluna in range(min, max):
                matriz[linha][coluna] += 1
        quadrante += 1

    resultado.append(matriz)

    dimensao = int(input())

for matriz in resultado:
    for linha in matriz:
        print("  ", end='')
        for index, coluna in enumerate(linha):
            if index == 0:

                print(coluna, end='')

            else:

                msg = ""
                qtdCaracteres = len(str(coluna))
                for i in range(qtdCaracteres, 4):
                    msg += " "
                print(msg + str(coluna), end='')

        print()
    print()