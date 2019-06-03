def fatorial(n):

    if n == 1:
        return 1
    else:
        return fatorial(n-1) * n


numero = int(input())

print(fatorial(numero))
