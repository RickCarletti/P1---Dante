entrada = int(input())

def preenche(numero):
    vetor = []
    vezes = 0
    cont = 0
    while vezes < 1000:
        vetor.append(cont)
        if cont >= numero-1: cont = 0
        else: cont += 1
        vezes += 1
    return vetor

saida = preenche(entrada)

for index, i in enumerate(saida):
    print("N[" + str(index) + "] = " + str(i))