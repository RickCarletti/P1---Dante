lista = list(map(float, input().split()))
somatorio = 0
listaAcimaDaMedia = []

for i in lista:
    somatorio += i
media = somatorio / len(lista)

for i in lista:
    if i > media: listaAcimaDaMedia.append(i)

print("Media = %.1f" % media)
print("Listagem dos numeros acima da media")
for i in listaAcimaDaMedia:
    print("    %.1f" % i)
print("Fim Listagem")
#421 343 543 76 675