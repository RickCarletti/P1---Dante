entrada= int(input())

def converte(x, b):
    resto = x % b
    divisao = x / b
    result = []
    while divisao >= 0:
        result.append(divisao)
        converte(divisao, b)
    return result

print(converte(13, 2))
