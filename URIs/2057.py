saida, duracao, fuso = map(int, input().split())

chegada = (24 + saida + duracao + fuso) % 24

print(chegada)
