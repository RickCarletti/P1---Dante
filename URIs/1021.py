def AchaNotas(val, listaA, listaB):
    retorno = []
    for i in listaA:
        notas = val // i
        retorno.append(notas)
        val -= notas*i

    for i in listaB:
        notas = val // i
        retorno.append(notas)
        val -= notas * i

    # print(round(val, 4))
    return retorno


listaDeNotas = [100, 50, 20, 10, 5, 2]
listaDeMoedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

entrada = 576.73 # float(input())

resultado = AchaNotas(entrada, listaDeNotas, listaDeMoedas)

tipo = 'nota(s)'

print('NOTAS:')
for index, tupla in enumerate(zip(resultado, list(listaDeNotas + listaDeMoedas))):

    if index == 6:
        tipo = 'moeda(s)'
        print('MOEDAS:')

    print(int(tupla[0]), tipo + ' de R$ %.2f' % tupla[1])
