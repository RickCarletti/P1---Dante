ranges = [[0,25], [25,50], [50,75], [75,100]]

def achaIntervalo(val, lista):
    max = lista[len(lista)-1]
    max = max[len(max)-1]
    min = lista[0][0]

    if min <= val <= max:
        for index, i in enumerate(lista):
            for j in i:
                if val <= j:
                    if index == 0:
                        return "Intervalo " + str(i).replace(" ", "")
                    else:
                        return "Intervalo " + str(i).replace("[", "(").replace(" ", "")

    else: return "Fora de intervalo"

valor = float(input())

resultado = achaIntervalo(valor, ranges)

print(resultado)