a, b, c = map(float, input().split())

delta = b**2 - 4*a*c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    xI  = (-b+delta**.5)/(2*a)
    xII = (-b-delta**.5)/(2*a)
    print("R1 =", round(xI, 5))
    print("R2 =", round(xII, 5))