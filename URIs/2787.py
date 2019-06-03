linha = int(input())
coluna = int(input())

cor = False

if linha % 2 == 0:
    cor = True
if coluna % 2 == 0:
    cor = not cor

if cor:
    print(0)
else:
    print(1)
