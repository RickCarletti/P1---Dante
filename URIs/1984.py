entrada = list(input().strip())

palavra = ''.join(entrada[::-1])

if 'e' in palavra:
    palavra = palavra[palavra.index('e')+1:]

print(palavra)