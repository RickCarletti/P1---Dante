dias = int(input())

ano = dias//365
mes = (dias - (ano*365)) // 30
dia = dias - (mes*30) - (ano*365)

print(ano, 'ano(s)')
print(mes, 'mes(es)')
print(dia, 'dia(s)')
