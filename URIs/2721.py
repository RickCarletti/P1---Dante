renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

qtdbolas = sum(list(map(int, input().split())))

print(renas[(qtdbolas-1) % 9])
