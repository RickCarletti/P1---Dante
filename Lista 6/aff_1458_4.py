teclado =[ [2, ['a','b','c','2']], [3, ['d','e','f','3']], [4, ['g','h','i','4']], [5, ['j','k','l','5']], [6, ['m','n','o','6']], [7, ['p','q','r','s','7']], [8, ['t','u','v','8']], [9, ['w','x','y','z','9']] ]
#1cm de lado, 30cm/s, .02s
xyTeclas = [[1,2,3],[4,5,6],[7,8,9],['_', 0, '#']]

cmPorSeg = 30
tempoDePressionar = .2

palavra = 'ad'

press = []

tempo = 0

# teclas cada e quantas vezes
prev = ''
for letra in palavra:
    for tecla in teclado:
        if letra in tecla[1]:
            if tecla[0] == prev:
                press.append(['#', 1])
                press.append([tecla[0], tecla[1].index(letra)+1])
                prev = tecla[0]
            else:
                press.append([tecla[0], tecla[1].index(letra) + 1])
                prev = tecla[0]

# print("Sequencia de teclas pressionadas, ex [tecla, vezes]: ", press)

# cada movimentos
movPolegar = []
prev = ''
for click in press:
        movPolegar.extend([click[0]]*click[1])

# print("Movimentos do polegar direito: ", movPolegar)

# coordenadas da tecla
def coordenada(mov):
    for linha in xyTeclas:
        for coluna in linha:
            if mov == coluna:
               return [xyTeclas.index(linha), linha.index(coluna)]
'''
# custo
def custoDeMovimento(I, F):
    coorIni = coordenada(I)
    coorFin = coordenada(F)
    xy = []
    custo = 0

    for i, f in zip(coorIni, coorFin):
        xy.append(abs(i-f))

    if not all(xy):
        for i in xy: custo += i
        return custo * tempoDe1cm
    else:
        hipotenusa = (xy[0] ** 2 + xy[1] ** 2) ** (1/2)
        return hipotenusa * tempoDe1cm
'''
# --------------------------------------------------------------------- AFF
def custoDeMovimento(I, F):
    coorIni, coorFin = coordenada(I), coordenada(F)
    linha, coluna = abs(coorIni[0] - coorFin[0]), abs(coorIni[1] - coorFin[1])
    xy = [linha, coluna]

    custo = 0

    if not all(xy):
        for i in xy:
            custo += i
        return custo / cmPorSeg
    else:
        hipotenusa = (xy[0] ** 2 + xy[1] ** 2) ** (1/2)
        return hipotenusa / cmPorSeg


# tempos
prevPolegarDireito = 6

for index, mov in enumerate(movPolegar):

    if mov in [4, prevPolegarDireito]:
        tempo += tempoDePressionar
        # print(mov, tempoDePressionar)
    else:
        tempo += custoDeMovimento(prevPolegarDireito, mov)
        tempo += tempoDePressionar
        # print(mov, custoDeMovimento(prevPolegarDireito, mov))
        # print(mov, tempoDePressionar)
        prevPolegarDireito = mov

print("  Teclas pressionadas -> [tecla, vezes]:  ", str(press).replace('[[', '[').replace(']]', ']'))
print("           Sequencia de pressionamentos:  ", movPolegar)

print("                                  Tempo:   %.2f" % tempo)
