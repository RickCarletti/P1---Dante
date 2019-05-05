DDD = [[61, "Brasilia"], [71, "Salvador"], [11, "Sao Paulo"], [21, "Rio de Janeiro"], [32, "Juiz de Fora"], [19, "Campinas"], [27, "Vitoria"], [31, "Belo Horizonte" ]]

entrada = int(input())
consta = False

for i in DDD:
    if entrada in i:
        print(i[1])
        consta = True

if not consta:
    print("DDD nao cadastrado")