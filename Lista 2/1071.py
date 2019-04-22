def pegaImpares(x):
    soma = 0
    if x == 1: return 1
    if x > 0:
        for i in range(0, x, 1):
            if i % 2 != 0:
                soma += i
        return soma
    else:
        return pegaImpares(abs(x))*-1
def somaImpares(x, y):
    if x == y: return 0
    if x > 0 and y > 0:
        if x > y: return x - y
        else: return y - x
    if x < 0:
        return somaImpares(abs(x), y)
    else: return somaImpares(x, abs(y))
a = int(input())
b = int(input())
resA = pegaImpares(a)
resB = pegaImpares(b)
print(somaImpares(resA, resB))