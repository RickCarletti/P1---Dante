meteoro = []
repetindo = True
aux = 0

while repetindo:
    x1, y1, x2, y2 = map(int, input().split())
    aux += 1

    if any([x1, y1, x2, y2]):
        qte = int(input())
        for i in range(qte):
            meteoro.append(list(map(int, input().split())))
            qte = 0
        for i in meteoro:
            if i[0] in range(x1, x2 + 1) and i[1] in range(y2, y1 + 1):
                qte += 1
        print("Teste " + str(aux))
        print(qte)
    else: repetindo = False