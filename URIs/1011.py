def Volume(raio):
    pi = 3.14159
    volume = (raio**3) * pi * (4/3)
    return volume

entrada = float(input())

saida = Volume(entrada)

print("VOLUME = %.3f" % saida)