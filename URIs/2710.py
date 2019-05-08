def ValidaMap(elemento):
    if elemento.isdigit(): return int(elemento)
    else: return elemento

def ValidaEntrada(A, B, C, D, val):
    listaDeValores = [A, B, C, D]
    if all(i >= 1 and i <= 500 for i in listaDeValores) and abs(val) <= 5000:
        return True

def CriaMatriz(linhas, colunas, valor):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor)
        matriz.append(linha)

    return matriz

matriz = CriaMatriz(500,500, 0)
saida = []
operacoes = int(input())

if operacoes <=100000:
    for i in range(operacoes):
        entrada = input().split()
        if entrada[0] == 'U':
            U, X1, Y1, X2, Y2, V = map(ValidaMap, entrada)
            if ValidaEntrada(X1, Y1, X2, Y2, V):
                for linha in range(len(matriz)):
                    if linha in range(X1, X2+1):
                        for coluna in range(len(matriz[0])):
                            if coluna in range(Y1, Y2+1):
                                matriz[linha][coluna] += V

        if entrada[0] == 'A':
            A, X, Y = map(ValidaMap, entrada)
            saida.append(matriz[X][Y])

for i in saida:
    print(i)