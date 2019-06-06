from math import ceil

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

    return retorno


listaDeNotas = [10000, 5000, 2000, 1000, 500, 200]
listaDeMoedas = [100, 50, 25, 10, 5, 1]

entrada = float(input())
entrada = ceil(entrada * 100)

resultado = AchaNotas(entrada, listaDeNotas, listaDeMoedas)

tipo = 'nota(s)'

print('NOTAS:')
for index, tupla in enumerate(zip(resultado, list(listaDeNotas + listaDeMoedas))):

    if index == 6:
        tipo = 'moeda(s)'
        print('MOEDAS:')

    print(int(tupla[0]), tipo + ' de R$ %.2f' % (tupla[1]/100))
