a = int(input('num1'))

listaDivisores = []

qtdDivisores = 0

for cont in range (2,a):
    if a % cont == 0:
        qtdDivisores = qtdDivisores + 1
        listaDivisores.append(cont)
if qtdDivisores == 0:
    print('e primo')
else:
    # print('lista de divisores',listaDivisores)
    for numero in listaDivisores:
        print(numero)

    for i in range(len(listaDivisores)):
        print(listaDivisores[i])