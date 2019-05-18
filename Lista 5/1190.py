entrada = input()
dimensao = 12
elementos = []
aux = 0

def fazMatriz(x):
    retorno = []
    for i in range(x):
        retorno.append([0]*x)
    return retorno


def constroiMatriz(x):
    retorno = []
    for linha in range(x):
        aux = []
        for coluna in range(x):
            aux.append(float(input()))
        retorno.append(aux)
    return retorno


matriz = constroiMatriz(dimensao)


for indexL, linha in enumerate(matriz):
    if indexL <= abs(dimensao/2)-1:
        for coluna in range(dimensao - indexL, dimensao):
            elementos.append(linha[coluna])
    elif indexL <= dimensao -2:
        for coluna in range(abs(dimensao - indexL - 12-1), dimensao):
            elementos.append(linha[coluna])

if entrada == 'S':
    aux = 0
    for i in elementos:
        aux += i
    print("%.1f" % aux)
elif entrada == 'M':
    aux = 0
    for i in elementos:
        aux += i
    aux /= len(elementos)
    print("%.1f" % aux)