'''
tabuleiroLinhas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
tabuleiroColunas = ['1', '2', '3', '4', '5', '6', '7', '8']

origem, destino = map(str, input().split())

origemValida = origem[0] in tabuleiroLinhas and origem[1] in tabuleiroColunas
destinoValido = destino[0] in tabuleiroLinhas and destino[1] in tabuleiroColunas

if origemValida and destinoValido:

    avancoLinha = abs(tabuleiroLinhas.index(origem[0]) - tabuleiroLinhas.index(destino[0]))
    avancoColuna = abs(tabuleiroColunas.index(origem[1]) - tabuleiroColunas.index(destino[1]))

    print(avancoLinha, avancoColuna)

    if sorted([avancoLinha, avancoColuna]) == [1, 2]:
        print('VALIDO')
    else:
        print('INVALIDO')
else:
    print('INVALIDO')
'''
tabuleiroLinhas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
tabuleiroColunas = ['1', '2', '3', '4', '5', '6', '7', '8']

movimento = input().split()

if all([False for mov in movimento for cord in mov if cord not in tabuleiroLinhas and cord not in tabuleiroColunas]):

    avancoLinha = tabuleiroLinhas.index(movimento[0][0]) - tabuleiroLinhas.index(movimento[1][0])
    avancoColuna = tabuleiroColunas.index(movimento[0][1]) - tabuleiroColunas.index(movimento[1][1])

    if sorted([abs(avancoLinha), abs(avancoColuna)]) == [1, 2]:
        print('VALIDO')
    else:
        print('INVALIDO')

else:
    print('INVALIDO')
