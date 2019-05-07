entradaCaixa = []
total = 0

for i in range(2):
    entradaCaixa.append(input().split())

for i in entradaCaixa:
    total += float(i[1]) * float(i[2])

print("VALOR A PAGAR: R$ %.2f" % total)