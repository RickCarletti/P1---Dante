mensagem = input()

if mensagem.count('1') % 2 != 0:
    mensagem += '1'
else:
    mensagem += '0'

print(mensagem)
