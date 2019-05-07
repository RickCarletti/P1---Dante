h, hh = map(int, input().split())

def ExtraiHoras(x):
    total = 0
    for i in range(24):
        if x <= i:
            total += 1
    return total

h = ExtraiHoras(h)
print(h)

hh = ExtraiHoras(hh)
print(hh)

print("O JOGO DUROU " + str(hh-h) + " HORA(S)")