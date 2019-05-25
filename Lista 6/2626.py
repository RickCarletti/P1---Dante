respostas = {'Dodô' : 'Os atributos dos monstros vao ser inteligencia, sabedoria...',
          'Leo' : 'Iron Maiden’s gonna get you, no matter how far!',
          'Pepper' : 'Urano perdeu algo muito precioso...',
           'empate' : 'Putz vei, o Leo ta demorando muito pra jogar...'}


def vence(A, B): return (A == 'pedra' and B == 'tesoura') or (A == 'papel' and B == 'pedra') or (A == 'tesoura' and B == 'papel')


def joga():
    if vence(dodo, pepper) and vence(dodo, leo):
        return respostas['Dodô']
    elif vence(leo, dodo) and vence(leo, pepper):
        return respostas['Leo']
    elif vence(pepper, dodo) and vence(pepper, leo):
        return respostas['Pepper']
    else:
        return respostas['empate']


while True:
    try:
        dodo, leo, pepper = map(str, input().split())
        print(joga())
    except:
        break
