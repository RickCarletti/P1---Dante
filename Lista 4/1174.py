entrada = []
for i in range(100):
    entrada.append(float(input()))

for index, i in enumerate(entrada):
    if i <= 10:
        indicie = str(index)
        valor = str(round(i, 1))
        print( "A[" + indicie + "] = " + valor )