entrada = int(input())

def preenche(val):
    resultado = []
    multi = val
    for i in range(10):
        resultado.append(multi)
        multi *= 2
    return resultado

saida =  preenche(entrada)
for index, i in enumerate(saida):
    print("N[" + str(index) + "] = " + str(i))