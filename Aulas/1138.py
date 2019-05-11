A, B = input().split()

while (int(A), int(B)) != (0, 0):

    digitos = [0]*10
    listaDeCaracteres = []
    numero = 0

    for i in range(int(A), int(B)+1):
        frase = str(i).split()
        for j in frase:
                listaDeCaracteres.extend(j)

    for index, linha in enumerate(digitos):
        digitos[index] = listaDeCaracteres.count(str(index))

    for index, i in enumerate(digitos):
        if index == 9:
            print(i)
        else: print(i, end=" ")

    A, B = input().split()