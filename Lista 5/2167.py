N = int(input())
listaValores = []

def ValidaEntradas(lista):
    for Ri in lista:
        if Ri in range(0, 10000+1):
            return True
        else:
            return False

def AchaQueda(lista):
    for index in range(len(lista)):
        if index == len(lista)-1:
            return 0
        if lista[index] > lista[index+1]:
            return index+2

if N in range(2, 100+1):
    listaValores.extend(list(map(int, input().split())))
    if ValidaEntradas(listaValores) and len(listaValores) == N:
            print(AchaQueda(listaValores))