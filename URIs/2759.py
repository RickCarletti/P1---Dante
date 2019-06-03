def permuta(vals, vezes):
    lista = vals
    if vezes == 0:
        return lista
    return permuta(lista[1:] + [lista[0]], vezes - 1)


valores = []
for i in range(3):
    valores.append(input())

aux = []

for i in range(3):
    aux = permuta(valores, i)
    print('A = ' + aux[0] + ', B = ' + aux[1] + ', C = ' + aux[2])
