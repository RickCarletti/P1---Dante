def felizes(): print(": )")
def tristes(): print(": (")

entradas = list(map(int, input().split()))

if not any((i >= -100) for i in entradas) and not any((i <= 100) for i in entradas):
    pass
else:
    print("????")

subiuNoSegundo, subiuNoSTerceiro, subiuMaisNoSegundo, cresceuIgual, constanteSegundo, constanteTerceiro, cresceuMais =  False, False, False, False, False, False, False

if entradas[0] < entradas[1]: subiuNoSegundo = True
if entradas[1] < entradas[2]: subiuNoSTerceiro = True
if (entradas[0] - entradas[1]) < (entradas[1] - entradas[2]) : cresceuMais = True
if (entradas[0] - entradas[1]) == (entradas[1] - entradas[2]) : cresceuIgual = True
if entradas[0] == entradas[1]: constanteSegundo = True
if entradas[1] == entradas[2]: constanteTerceiro = True

if constanteSegundo:
    if subiuNoSTerceiro: felizes()
    elif not subiuNoSTerceiro: tristes()
else:
    if subiuNoSegundo:
        if not subiuNoSTerceiro or constanteTerceiro: tristes()
        elif subiuNoSTerceiro:
            if not cresceuMais: felizes()

            elif cresceuIgual or cresceuMais: tristes()
    elif not subiuNoSegundo:
        if subiuNoSTerceiro or constanteTerceiro: felizes()
        elif not subiuNoSTerceiro:
            if cresceuMais or cresceuIgual: tristes()
            elif not cresceuMais or not cresceuIgual: felizes()