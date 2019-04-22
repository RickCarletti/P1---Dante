nota = list(map(float, input().split()))
media = ((nota[0]*2)+(nota[1]*3)+(nota[2]*4)+(nota[3]))/(2+3+4+1)
print("Media:", "%.1f" % media)
if media >= 7: print("Aluno aprovado")
elif media <= 6.9 and media >= 5:
    print("Aluno em exame")
    notaExame = float(input())
    print("Nota do exame:", "%.1f" % notaExame)
    media = (media + notaExame) / 2
    if media > 4.9:
        print("Aluno aprovado")
        print("Media final:", "%.1f" % media)
    else: print("Aluno reprovado")
else: print("Aluno reprovado")