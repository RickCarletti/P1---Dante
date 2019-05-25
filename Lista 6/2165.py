texto = len(input())

valido = 1 <= texto <= 140

if valido:
    print('TWEET')
else:
    print('MUTE')