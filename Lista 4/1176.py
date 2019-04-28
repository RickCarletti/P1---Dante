def fibonacci(n):
    f = ((1+(5**.5))/2)**n
    f = f - ((1-(5**.5))/2)**n
    f = f / (5**.5)
    return f


vetor = []
casos = int(input())

for i in range(casos):
    vetor.append(float(input()))


if True:
    saida = []
    aux = 0
    for index, i in enumerate(vetor):
        if index > 1:
            aux += fibonacci(i)

            saida.append(aux)
        else:
            aux += fibonacci(index)

    for index, i in enumerate(saida):
        print( "Fib(" + str(index) + ") = " + str(i) )


