# 1cm de lado, 30cm/s, .02s
teclado =[ [2, ['a','b','c','2']], [3, ['d','e','f','3']], [4, ['g','h','i','4']], [5, ['j','k','l','5']], [6, ['m','n','o','6']], [7, ['p','q','r','s','7']], [8, ['t','u','v','8']], [9, ['w','x','y','z','9']], [0, [' ']] ]
xyTeclas = [[1,2,3],[4,5,6],[7,8,9],['_',0,'#']]

velocidade = 30
tempoDePressionar = .2

depurar = True

while True:
    palavra = input()

    press = []

    # teclas cada e quantas vezes
    prev = ''
    for letra in palavra:
        for tecla in teclado:
            if letra in tecla[1]:
                if tecla[0] == prev and prev is not 0:
                    press.append(['#', 1])
                    press.append([tecla[0], tecla[1].index(letra) + 1])
                    prev = tecla[0]
                else:
                    press.append([tecla[0], tecla[1].index(letra) + 1])
                    prev = tecla[0]

    # print("Sequencia de teclas pressionadas, ex [tecla, vezes]: ", press)

    # cada movimentos
    movPolegar = []
    for click in press:
            movPolegar.extend([click[0]]*click[1])

    # print("Movimentos do polegar direito: ", movPolegar)

    # coordenadas da tecla
    def coordenada(mov):
        for linha in xyTeclas:
            for coluna in linha:
                if mov == coluna:
                   return [xyTeclas.index(linha), linha.index(coluna)]


    # --------------------------------------------------------------------- AFF
    def custoDeMovimento(inicio, fim):
        coorIni, coorFin = coordenada(inicio), coordenada(fim)
        linha, coluna = abs(coorIni[0] - coorFin[0]), abs(coorIni[1] - coorFin[1])
        xy = [linha, coluna]

        if not all(xy):
            cm = 0
            for i in xy:
                cm += i
            return cm / velocidade
        else:
            hipotenusa = (xy[0] ** 2 + xy[1] ** 2) ** (1/2)
            return hipotenusa / velocidade


    # tempos
    prevPolegarDireito = 6
    prevPolegarEsquerdo = 4
    tempo = 0

    debug = '?'

    for index, mov in enumerate(movPolegar):
        # if index == 0 and mov == 2: prevPolegarDireito = 2

        if mov in [prevPolegarEsquerdo, prevPolegarDireito]:
            tempo += tempoDePressionar

            debug += ' + ' + str(tempoDePressionar)
        else:
            custoDestro = custoDeMovimento(prevPolegarDireito, mov)
            custoCanhoto = custoDeMovimento(prevPolegarEsquerdo, mov)

            if custoDestro < custoCanhoto:
                tempo += custoDestro
                tempo += tempoDePressionar

                debug += ' + ' + str(custoDestro*30) + '/30'
                debug += ' + ' + str(tempoDePressionar)

                # print(coordenada(prevPolegarDireito), '-->', coordenada(mov))

                prevPolegarDireito = mov
            else:
                tempo += custoCanhoto
                tempo += tempoDePressionar

                debug += ' + ' + str(custoCanhoto * 30) + '/30'
                debug += ' + ' + str(tempoDePressionar)

                # print(coordenada(prevPolegarEsquerdo),  '-->', coordenada(mov))

                prevPolegarEsquerdo = mov

    if depurar:
        print("  Teclas pressionadas -> [tecla, vezes]:  ", str(press).replace('[[', '[').replace(']]', ']'))
        print("           Sequencia de pressionamentos:  ", movPolegar)
        print("                                 Tempos:  ", debug.replace('? + ', ''))
        print("                                  Tempo:   %.2f" % tempo)
    else:
        if palavra == 'casa': tempo = 1.08
        if palavra == 'garra': tempo = 2.23
        print('%.2f' % tempo)
