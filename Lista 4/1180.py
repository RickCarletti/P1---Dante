tamanho = int(input())
lista = list(map(int, input().split()))
menor = min(lista)

for index, i in enumerate(lista):
    if menor == i:
        print("Menor valor: " + str(menor))
        print("Posicao: " + str(index))