A, B = map(int, input().split())

if A > B: resto = A % B
if A < B: resto = B % A

if resto == 0: print("Sao Multiplos")
else: print("Nao sao Multiplos")