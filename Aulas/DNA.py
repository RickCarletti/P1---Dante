def geraDNA(tam):
    from random import randint
    frase = ""
    baseNitrogenada = "CGAT"
    for i in range(tam):
        frase += baseNitrogenada[randint(0, len(baseNitrogenada)-1)]
    return frase

def examinaDNA(pDNA, dDNA, n):
    if pDNA.count(dDNA) >= n:
        return True
    else:
        return False

tamDnaPessoa = int(input())
tamDnaDoeca = int(input())
qtdeOcorrencias = int(input())

dnaPessoa = geraDNA(tamDnaPessoa)
dnaDoenca = geraDNA(tamDnaDoeca)

if examinaDNA(dnaPessoa, dnaDoenca, qtdeOcorrencias):
    print("Doente")
else:
    print("...")