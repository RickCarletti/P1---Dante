def AchaNotas(val, lista):
    retorno = []
    for i in lista:
        notas = int(val/i)
        retorno.append(notas)
        val -= notas*i
    return retorno
listaDeNotas = [50, 10, 5, 1]
entrada = int(input())
resultado = AchaNotas(entrada, listaDeNotas)
for i in resultado:
    print(i, end=" ")