leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

for vezes in range(int(input())):

    entrada = input()
    qtdLeds = 0

    for char in entrada:
        qtdLeds += leds[char]

    print(qtdLeds, 'leds')
