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


for index, linha in enumerate(matriz):
    max = index
    max2 = dimensao - index - 1
    if index <= abs(dimensao/2)-1:
        elementos.extend(linha[0:max])
    else:
        elementos.extend(linha[0:max2])

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