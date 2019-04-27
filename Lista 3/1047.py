hI, mI, hII, mII = map(int, input().split())

diferencaDeHoras = hII - hI
diferencaDeMinutos = mII - mI

minutos = (diferencaDeHoras * 60) + diferencaDeMinutos
horas = int(minutos/60)
minutos =  abs(minutos - (horas * 60))

if hI == hII and mI == mII:
    horas = 24
    minutos = 0
elif diferencaDeHoras == 0 and diferencaDeMinutos < 0:
    horas = 23
    minutos = 60 + diferencaDeMinutos
elif diferencaDeMinutos == 0 and diferencaDeHoras < 0:
    horas = 24 - abs(horas)
elif diferencaDeHoras < 0 and diferencaDeMinutos < 0:
    horas = 23 + horas
    minutos = 60 - minutos
elif diferencaDeHoras < 0 and diferencaDeMinutos > 0:
    horas = 23
    minutos = 60 - minutos

print("O JOGO DUROU " + str(horas) + " HORA(S) E " + str(minutos) + " MINUTO(S)")

'''
    def faz(k):
    hI, mI, hII, mII = map(int, k)

    diferencaDeHoras = hII - hI
    diferencaDeMinutos = mII - mI

    minutos = (diferencaDeHoras * 60) + diferencaDeMinutos
    horas = int(minutos/60)
    minutos =  abs(minutos - (horas * 60))

    if hI == hII and mI == mII:
        horas = 24
        minutos = 0
    elif diferencaDeHoras == 0 and diferencaDeMinutos < 0:
        horas = 23
        minutos = 60 + diferencaDeMinutos
    elif diferencaDeMinutos == 0 and diferencaDeHoras < 0:
        horas = 24 - abs(horas)
    elif diferencaDeHoras < 0 and diferencaDeMinutos < 0:
        horas = 23 + horas
        minutos = 60 - minutos
    elif diferencaDeHoras < 0 and diferencaDeMinutos > 0:
        horas = 23
        minutos = 60 - minutos

    print("O JOGO DUROU " + str(horas) + " HORA(S) E " + str(minutos) + " MINUTO(S)")

faz([1,1,1,1])
faz([1,1,1,0])
faz([1,1,0,1])
faz([1,0,1,1])
faz([0,1,1,1])
print("---------------------------------------")
faz([0,0,0,1])
faz([0,0,1,0])
faz([0,1,0,0])
faz([1,0,0,0])
print("---------------------------------------")
faz([1,1,0,0])
faz([1,0,0,1])
faz([0,0,1,1])
print("---------------------------------------")
faz([1,0,1,0])
faz([0,1,0,1])
faz([0,1,0,1])
'''