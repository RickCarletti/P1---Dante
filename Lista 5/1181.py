def constroiMatriz(x):
    retorno = []
    for linha in range(x):
        aux = []
        for coluna in range(x):
            aux.append(float(input()))
        retorno.append(aux)
    return retorno


L = int(input())
T = input()

matriz = constroiMatriz(12)

elementos = []

if L >=0 and L <=11:
    for i in matriz[L]:
        elementos.append(i)

    if T == 'S':
        aux = 0
        for i in elementos:
            aux += i
        print("%.1f" % aux)
    elif T == 'M':
        aux = 0
        for i in elementos:
            aux += i
        aux /= len(elementos)
        print("%.1f" % aux)