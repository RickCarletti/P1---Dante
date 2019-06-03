cardapio = {1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005: 5.50}

total = 0

for i in range(int(input())):
    codigo, qtd = map(int, input().split())
    total += qtd * cardapio[codigo]

print('%.2f' % total)
