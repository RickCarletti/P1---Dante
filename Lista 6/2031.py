listaDeRespostas = {'jogador1': 'Jogador 1 venceu', 'jogador2': 'Jogador 2 venceu', 'ataque': 'Aniquilacao mutua', 'pedra': 'Sem ganhador', 'papel': 'Ambos venceram'}
listaDeValidacao = {'pedra', 'papel', 'ataque'}


def validaEntradas(tam, entradas, validacoes):
    if not entradas:
        return 'EOF'
    if len(entradas) != tam or [False for entrada in entradas if entrada not in validacoes]:
        return False
    else:
        return [entradas[0], entradas[1]]


def vencedor(jogadas, lista):

    def vence(A, B):
        return (A == 'ataque' and B == 'pedra') or (A == 'pedra' and B == 'papel') or (A == 'ataque' and B == 'papel') or (A == B)

    jogador1, jogador2 = jogadas[0], jogadas[1]
    resposta = lista

    resultadoA, resultadoB = vence(jogador1, jogador2), vence(jogador2, jogador1)

    if resultadoA == resultadoB:
        if jogador1 == 'ataque': return resposta['ataque']
        if jogador1 == 'pedra': return resposta['pedra']
        if jogador1 == 'papel': return resposta['papel']
    elif resultadoA: return resposta['jogador1']
    else: return resposta['jogador2']


for vez in range(int(input())):

    entradas = validaEntradas(2, [input(), input()], listaDeValidacao)

    if entradas not in [False, 'EOF']:
        print(vencedor(entradas, listaDeRespostas))