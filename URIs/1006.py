def trata(val): return round(float(val), 1)


listaPesos = [2, 3, 5]
media = 0
peso = 0

for i in listaPesos:
    peso += i
    media += trata(input()) * i

print("MEDIA = " + str(round(media/peso, 1)))
