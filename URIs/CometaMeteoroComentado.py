meteoro = []
repetindo = True
aux = 0

while repetindo:
    x1, y1, x2, y2 = map(int, input().split())
    aux += 1                    #contagem do while para imprimir no teste

    if any([x1, y1, x2, y2]):   #any(lista) testa se algum dos valores da lista é verdadeiro, se for, ele retorna verdade; Lembrando que para teste boleano de inteiro, == 0 é False e != 0 é True...
        qte = int(input())      #recebe quantidade de meteoros a serem testados
        for i in range(qte):    #itera quantas vezes houverem meteoros
            '''
            Poderia ser assim, é até mais facil pra visualizar, mas eu prefiro sair tacando tudo que nem fiz em baixo...
            
            novasCoordenadas = map(int, input().split())
            meteoro.append(novasCoordenadas)
            
            '''
            meteoro.append(list(map(int, input().split())))     # lista 'meteoro' aprende um par de cordenadas [x, y] de um novo meteoro.
                                                                # Exatamente o que tá ali em cima de verde, mas pra tacar um map dentro de um append tem que colocar ele como lista:
                                                                # append list map...
                                                                # append(   list(    map()   )   )

        qte = 0 # Como a quantidade de metoros já foi apreciada, utilizo a variavel para outro fim, e pra isso, antes eu zero ela. Isso ajuda a diminuir a memoria que o programa ocupa

        for i in meteoro:      # itera sobre a quatidade de cordenadas aprendidas em 'meteoro'; Nesse caso, as cordenadas sao uma lista dentro da lista 'meteoro', por isso i é um par valores e não um valor único...
                               # logo em cada iteração de i, i será uma lista [x, y]

            if i[0] in range(x1, x2+1) and i[1] in range(y2, y1+1): # agora que a mágica acontece, e ela se chama range() ...
                qte += 1                                            # Essa macumba retorna uma lista de valores que está entre limites colocados nela como parametros...
                                                                    # range(a) = [0 ... a]
                                                                    # range(a, b) == [a ... b]
                                                                    # então ...
                                                                    # if       i[0]       in       range(x1, x2+1)
                                                                    # se        [x]       estiver  entre(x1 e x2) : pow
        print("Teste " + str(aux))
        print(qte)
    else: repetindo = False