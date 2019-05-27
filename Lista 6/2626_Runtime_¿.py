listaDeRespostas = {'Dodô' : 'Os atributos dos monstros vao ser inteligencia, sabedoria...', 'Leo' : 'Iron Maiden’s gonna get you, no matter how far!', 'Pepper' : 'Urano perdeu algo muito precioso...', 'empate' : 'Putz vei, o Leo ta demorando muito pra jogar...'}
listaDeValidacao = {'pedra', 'papel', 'tesoura'}


def validaEntradas(tam, entradas, validacoes):
    if not entradas:
        return 'EOF'
    elif len(entradas) != tam or [False for entrada in entradas if entrada not in validacoes]:
        return False
    else:
        return [entradas[0], entradas[1], entradas[2]]


def vencedor(ordemDLP, lista):
    def vence(A, B): return (A == 'pedra' and B == 'tesoura') or (A == 'papel' and B == 'pedra') or (A == 'tesoura' and B == 'papel')
    dodo, leo, pepper = ordemDLP[0], ordemDLP[1], ordemDLP[2]
    resp = lista
    if vence(dodo, pepper) and vence(dodo, leo): return resp['Dodô']
    elif vence(leo, dodo) and vence(leo, pepper): return resp['Leo']
    elif vence(pepper, dodo) and vence(pepper, leo): return resp['Pepper']
    else: return resp['empate']


validas = False

while validas is not 'EOF':

    validas = validaEntradas(3, input().split(), listaDeValidacao)

    if validas not in [False, 'EOF']:
        print(vencedor(validas, listaDeRespostas))