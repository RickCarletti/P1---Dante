def fibonacci(n):
    f = ((1+(5**.5))/2)**n
    f = f - ((1-(5**.5))/2)**n
    f = f / (5**.5)
    return f

listaFibonacci = []

for i in range(61):
    listaFibonacci.append(fibonacci(i))

vezes = int(input())

for i in range(vezes):
    indicie = int(input())
    print("Fib(" + str(indicie) + ") = " + str(int(listaFibonacci[indicie])))