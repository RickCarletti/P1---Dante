for caso in range(int(input())):
    A, B = map(int, input().split())

    if B == 0: print('divisao impossivel')
    elif A == 0: print('0.0')
    else:
        print(A/B)
