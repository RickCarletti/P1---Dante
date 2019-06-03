T1, T2, T3, T4 = map(int, input().split())

extencoes = sorted([T1, T2, T3, T4])

quatidades = []

for regua in extencoes:

    quantidade = regua-3

    listaAuxiliar = extencoes.copy()
    listaAuxiliar.pop(listaAuxiliar.index(regua))
    listaAuxiliar.sort()
    listaAuxiliar.reverse()

    if regua > 3: regua = 3

    for i in range(regua):
        quantidade += listaAuxiliar[i]

    quatidades.append(quantidade)

print(max(quatidades))
