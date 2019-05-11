auxI, auxJ = 0, 0

for i in range(0, int(2/.2)+1, 1):

    for j in range(1, 4, 1):
        auxJ = j + auxI
        print("I={} J={}".format(auxI, auxJ))

    auxI = round(auxI + 0.2, 1)