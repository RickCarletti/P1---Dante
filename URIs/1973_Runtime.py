estrelas = int(input())

listaDeCarneiros = list(map(int, input().split()))

def ePar(x):
    return True if x % 2 is 0 else False


def roubaCarneiro(vals, pos, conhecidas=''):
    # a = list(a)
    lista = []
    lista.extend(vals)

    if not (pos < 0 or pos > len(lista)-1 or lista[pos] is 0):

        prevV = lista[pos]

        lista[pos] -= 1

        if ePar(prevV):
            return roubaCarneiro(lista, pos - 1, conhecidas + str(pos))
        else:
            return roubaCarneiro(lista, pos + 1, conhecidas + str(pos))

    return lista, conhecidas


if len(listaDeCarneiros) == estrelas:
    listaDeCarneirosRoubados = roubaCarneiro(listaDeCarneiros, 0)

    roubados = sum(listaDeCarneirosRoubados[0])

    print(len(set(listaDeCarneirosRoubados[1])), roubados)