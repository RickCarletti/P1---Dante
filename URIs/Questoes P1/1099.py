entrada = int(input())

for i in range(entrada):
    soma = 0
    A, B = map(int, input().split())

    if A >= B: A, B = B, A

    for impar in range(A+1, B):
        if impar % 2 != 0:
            soma += impar
    print(soma)