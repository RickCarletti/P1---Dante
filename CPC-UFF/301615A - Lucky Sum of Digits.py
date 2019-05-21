luckyDigits = [4, 7]

def hasLucky(num, lista):
    lMin = 0
    A = 0
    for l in lista: lMin += l
    if num < lMin: return -1

    x = num-1

def hasLucky2(num, lista, pos):
    lista.sort()

    resultado = []

    if pos == 0: return resultado

    restoDoMaior = num % lista[pos-1]
    divisaoDoMaior = num // lista[pos-1]

    if isinstance(restoDoMaior, int) and divisaoDoMaior < lista[pos-2]:
        return -1
    else:
        print(restoDoMaior)
        resultado.append(restoDoMaior)
        hasLucky2(num, lista, pos-1)




entrada = input()

print(hasLucky2(entrada, luckyDigits, len(str(entrada))-1))


