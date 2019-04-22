nVezes = int(input())
rI = list(map(int, input().split()))
mary = 0
jhon = 0
for x in range(nVezes):
    if rI[x] == 0: mary += 1
    if rI[x] == 1: jhon += 1
print("Mary won", mary,"times and Jhon won", jhon, "times")