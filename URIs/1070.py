imparesConsecutivos = []

numero = int(input())

while len(imparesConsecutivos) is not 6:

    if numero % 2 != 0:
        imparesConsecutivos.append(numero)

    numero += 1

for impar in imparesConsecutivos:
    print(impar)
