def car(lista): #      ???????????/
    return lista[0]


def cdr(lista): #    ???????????????
    return lista[1:]


def cons(el, lista):
    return [el] + lista


def rodaLista(lista, vezes):
    if vezes is 0:
        return lista
    else:
        return rodaLista(cons(lista[-1], lista[:-1]), vezes - 1)


saida = ['a', 'b', 'c', 'd']


print(rodaLista(saida, 0))
print(rodaLista(saida, 1))
print(rodaLista(saida, 2))
print(rodaLista(saida, 3))