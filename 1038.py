leia = list(map(int, input().split()))
if leia[0] == 1 : print("Total: R$", "%.2f" % (leia[1]*4))
if leia[0] == 2 : print("Total: R$", "%.2f" % (leia[1]*4.5))
if leia[0] == 3 : print("Total: R$", "%.2f" % (leia[1]*5))
if leia[0] == 4 : print("Total: R$", "%.2f" % (leia[1]*2))
if leia[0] == 5 : print("Total: R$", "%.2f" % (leia[1]*1.5))