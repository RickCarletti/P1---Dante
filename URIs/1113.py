A, B = map(int, input().split())

while A != B:
    print('Crescente') if B > A else print('Decrescente')
    A, B = map(int, input().split())
