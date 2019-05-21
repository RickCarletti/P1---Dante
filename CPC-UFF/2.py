digitosDaSorte = [4, 7]

def temSorte(num, lista):
    lista.reverse()
    resultado = []
    B = num
    cont = 1

    while B >= lista[-2]:

        A = num - lista[-1] * cont

        B = int(A / lista[-2])

        Br = A % lista[-2]

        if Br == 0:
            if B > cont:
                B, cont = cont, B
            resultado.extend([cont, B])
            return resultado

        cont += 1

    return -1


while True:
    entrada = int(input())

    saida = temSorte(entrada, digitosDaSorte)

    if saida != -1:
        for dig, vezes in zip(digitosDaSorte, saida):
            print(str(dig) * vezes, end='')