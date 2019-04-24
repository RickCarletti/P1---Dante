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

entrada = list(map(float, input().split()))

entradaOrdenada = ordenaSimples(entrada, False)

A, B, C = map(float, entradaOrdenada)
sum = lambda x, y, z: x + y + z

if A > 0 and B > 0 and C > 0:
    if (B - C) < A < (B + C) or (A - C) < B < (A + C) or (A - B) < C < (A + B):
        perimetro = sum(A, B, C)
        print("Perimetro = %.1f" % perimetro)
    else:
        area = ((A+B)/2)*C
        print("Area = %.1f" % area)