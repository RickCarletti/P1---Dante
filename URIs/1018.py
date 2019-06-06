def AchaNotas(val, lista):
    retorno = []
    for i in lista:
        notas = int(val/i)
        retorno.append(notas)
        val -= notas*i
    return retorno

listaDeNotas = [100, 50, 20, 10, 5, 2, 1]

entrada = int(input())

resultado = AchaNotas(entrada, listaDeNotas)

print(entrada)
for tupla in zip(resultado, listaDeNotas):
    print(tupla[0], 'nota(s) de R$', str(tupla[1])+',00')
