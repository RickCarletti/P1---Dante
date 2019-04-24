def achaHip(h, c1, c2):
    if h > c1 and h > c2: return h
    if c1 > c2: return achaHip(c1, h, c2)
    if c2 > c1: return achaHip(c2, h, c1)

def ordenaSimples(vetor, sen):
    tamanhoVetor = len(vetor)-1
    ordenando = True
    while ordenando:
        ordenando = False
        for i in range(tamanhoVetor):
            if sen:
                if vetor[i] > vetor[i+1]:
                    vetor[i], vetor[i+1] = vetor[i+1],vetor[i]
                    ordenando = True
            else:
                if vetor[i] < vetor[i + 1]:
                    vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                    ordenando = True
    return vetor

#transformar list em array
lista = list(map(int, input().split()))
listaInt = []
for i in range(len(lista)): listaInt.append(int(lista[i]))

    if permaneceuConstanteNoSegundoDia and dif:
        felizes()
        break
    if permaneceuConstanteNoSegundoDia and dif: felizes()

    if not subiuNoPrimeiroDia and subiuNoSegundoDia or eq: felizes()
    if not subiuNoPrimeiroDia and not subiuNoSegundoDia and not dif: felizes()
    if not subiuNoPrimeiroDia and not subiuNoSegundoDia and eq or dif:tristes()

    if subiuNoPrimeiroDia and not subiuNoSegundoDia or permaneceuConstanteNoTerceiroDia: tristes()
    if subiuNoPrimeiroDia and subiuNoSegundoDia and not dif: tristes()
    if subiuNoPrimeiroDia and subiuNoSegundoDia and eq or dif: felizes()

elif subiuNoSegundo:
if not subiuNoSTerceiro or constanteTerceiro:
    tristes()
elif subiuNoSTerceiro:
    if not cresceuMais:
        tristes()
    elif cresceuIgual or cresceuMais:
        felizes()

elif not subiuNoSegundo:
    if subiuNoSTerceiro or constanteTerceiro:
        felizes()
    elif not subiuNoSTerceiro:
        if not cresceuMais:
            felizes()
        elif cresceuIgual or cresceuMais:
            tristes()