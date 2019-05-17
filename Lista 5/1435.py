dimensao = int(input())

def fazMatriz(x):
    retorno = []
    for i in range(x):
        retorno.append([0]*x)
    return retorno


while dimensao > 0:

    matriz = fazMatriz(dimensao)
    quadrante = 0

    while quadrante != dimensao:
        max = dimensao - quadrante
        min = quadrante
        for linha in range(min, max):
            for coluna in range(min, max):
                matriz[linha][coluna] +=1
        quadrante += 1

    for linha in matriz:
        print("  ", end='')
        for index, coluna in enumerate(linha):
            if not index == len(linha)-1:
                print(coluna, end="   ")
            else:
                print(coluna)
    print()

    dimensao = int(input())
