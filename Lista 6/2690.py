mapaDeCaracteres = {0: ['a', 'k', 'u', 'G', 'Q'], 1: ['b', 'l', 'v', 'I', 'S'], 2: ['c', 'm', 'w', 'E', 'O', 'Y'], 3: ['d', 'n', 'x', 'F', 'P', 'Z'], 4: ['e', 'o', 'y', 'J', 'T'], 5: ['f', 'p', 'z', 'D', 'N', 'X'], 6: ['g', 'q', 'A', 'K', 'U'], 7: ['h', 'r', 'C', 'M', 'W'], 8: ['i', 's', 'B', 'L', 'V'], 9: ['j', 't', 'H', 'R']}
lista, saidas = [], []
lista.extend(mapaDeCaracteres.items())

vezes = int(input())

for vez in range(vezes):

    saida = ''

    frase = ''.join([x for index, x in enumerate(input().replace(' ', '')) if index < 13])

    for caractere in frase:

        saida += str([obj[0] for obj in lista if caractere in obj[1]]).replace('[', '').replace(']', '')

        if len(saida) == 12:
            saidas.append(saida)
            break

if saidas:
    for i in saidas:
        print(i)
