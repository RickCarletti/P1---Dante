vezes = int(input())

for vez in range(vezes):

    palavra = input()

    tempo = 0

    tempo += .01 * len(palavra)

    print("%.2f" % tempo)
