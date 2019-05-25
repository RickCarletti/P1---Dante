vezes = int(input())

for vez in range(vezes):
    paridade = False

    frase = list(map(str, input().split()))

    A, B = map(int, input().split())

    if (A + B) % 2 == 0:
        paridade = 'PAR'
    else:
        paridade = 'IMPAR'

    x = frase[frase.index(paridade)-1]
    print(x)
