listaDePrimos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def fatPrimos(n):

    if n <= 0:
        return [0]
    elif n == 1:
        return [1]
    else:
        lista = []
        for i in range(2, n + 1):
            while n % i == 0:
                n = n / i
                lista.append(i)
        return lista


potencias = []

for n in range(1, 101):

    N = fatPrimos(n)

    potencias = [f - 1 for f in N]
    potencias.reverse()

    resultados = []
    saida = 1

    for index, pot in enumerate(potencias):
        saida *= listaDePrimos[index] ** pot

    print(saida % 1000000007)