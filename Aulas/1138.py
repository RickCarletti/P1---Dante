A, B = input().split()

while (A, B) != (0, 0):
    digitos = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]
    listaDeCaracteres = []
    numero = 0

    for i in range(int(A), int(B)+1):
        frase = str(i).split()
        for j in frase:
                listaDeCaracteres.extend(j)

    for linha in digitos:
        linha[1] = listaDeCaracteres.count(str(linha[0]))

    for i in digitos:
        print(i[1], end=" ")
    print()

    A, B = input().split()