def basca(a, b, c, dec):
    try:
        delta = (b ** 2) - 4 * a * c
        xI, xII = float, float
        xI = round(((-1 * b) + delta ** .5) / (2 * a), dec)
        xII = round(((-1 * b) - delta ** .5) / (2 * a), dec)
        return xI, xII

    except ValueError:
        print("Impossivel calcular")

    except ZeroDivisionError:
        print("Impossivel calcular")

a, b, c = map(float, input().split())

resultado = basca(a, b, c, 5)

if resultado:
    print("R1 = ", resultado[0])
    print("R1 = ", resultado[1])