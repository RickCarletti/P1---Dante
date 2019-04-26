lista = ("[0,25], (25,50], (50,75], (75,100]")
intervalos = []
x = []

intervalos = lista.split(" ")
intervalosF = []
for i in intervalos:
    x.clear()
    for j in i:
        x.append(j.replace("[", "").replace("(", "").replace(' ', '').replace(']', '').replace(')', ''))
    intervalosF.append(x)

for i in intervalosF:
    if not i: 
print(intervalosF)