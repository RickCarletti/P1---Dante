lista = ("[0,25], (25,50], (50,75], (75,100]")
matriz = []
aux_m = []
aux = ""
numeros = []

for i in lista:
    if i.isdigit():
        aux += i
    elif aux is not "":
        numeros.append(aux)
        aux = ""

for index, i in enumerate(numeros):
    aux_m.append(i)
    if index % 2:
        matriz.append(list(aux_m))
        aux_m = []

print(matriz)