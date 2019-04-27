numero = int(input())

def PUM(x, mult):
    res = []
    aux = 1
    frase = ""
    for i in range(x):
        frase = ""
        for j in range(aux, aux+mult-1):
            aux = j
            frase += str(j) + " "
        aux += 2
        frase += "PUM"
        res.append(frase)
    return res

resultado = PUM(numero, 4)

for i in resultado:
    print(i)