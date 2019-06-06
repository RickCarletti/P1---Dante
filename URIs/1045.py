catetos = list(map(float, input().split()))

catetos.reverse()

print(catetos)
A, B, C = map(float, [i for i in catetos])

if A >= B + C:
    print('NAO FORMA TRIANGULO')
