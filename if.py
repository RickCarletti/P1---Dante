def pegaImpares(x):
    soma = 0
    if x > 0:
        for i in range(0, x, 1):
            if i % 2 != 0:
                soma += i
        return soma
    elif x < 0:
        return pegaImpares(abs(x))*-1

a = int(input())
b = int(input())
resA=pegaImpares(a)
resB=pegaImpares(b)
print("pegaImpares de a", resA)
print("pegaImpares de b", resB)
print("Saida =", resA+resB)
