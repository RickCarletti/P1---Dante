def fibonacci(n):
    r5 = 5**.5
    fb1 = ((1+r5)/2)**n
    fb2 = ((1-r5)/2)**n
    f = (fb1 - fb2) / r5
    return f
entrada = float(input())
if entrada > 0 and entrada <= 50:
    print(round(fibonacci(entrada), 1))