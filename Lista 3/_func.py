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

