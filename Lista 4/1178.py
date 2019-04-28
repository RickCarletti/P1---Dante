vetor = []
x = float(input())

for i in range(100):
    vetor.append(x)
    x /= 2

for index, i in enumerate(vetor):
    print("N[" + str(index) + "] = " + "%.4f" % i, sep='')